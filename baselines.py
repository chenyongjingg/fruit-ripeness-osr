#!/usr/bin/env python3
"""Zero-shot baselines: CLIP (open-vocabulary) and Qwen2-VL (generative VLM).

Both write results in the same JSON schema as E1/E2 so report.py can aggregate them.

Protocol notes
--------------
* CLIP: frozen image tower + text prompts; prediction = argmax over class prompts,
  averaged over a small template set. No tuning on test data.
* Qwen2-VL: greedy decoding, fixed prompt. Zero-shot = one image per request.
  5-shot = five labelled exemplars per class in the same conversation.
  Unparseable outputs are kept as a distinct "__unparsed__" prediction (they count
  as errors in accuracy/macro-F1) and their rate is reported separately — they are
  never silently dropped.
"""
import argparse, json, os, re, sys, time, hashlib, math
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import PROC, RESULTS, log, atomic_write_json, read_json, sha256_ids, CODE_VERSION
from rio.methods import closed_set_metrics


def _meta(ds):
    return pd.read_csv(PROC / ds / "meta.csv")


def _paths(m):
    return [str(PROC / p) for p in m["path"]]


def _cap(te, labels, max_n, seed=0):
    if not max_n or len(te) <= max_n:
        return te.reset_index(drop=True)
    per = max(1, int(math.ceil(max_n / len(labels))))
    out = te.groupby("label_name", group_keys=False).apply(
        lambda g: g.sample(min(len(g), per), random_state=seed))
    return out.reset_index(drop=True)


def display_names(labels, fruit):
    """Strip the fruit word from a class label so templates do not say "banana ... banana".

    "Banana_Unripe" with fruit="banana" -> "unripe"; "underripe" -> "underripe".
    Returns {display: original_label}.
    """
    fr = fruit.replace("_", " ").lower()
    out = {}
    for c in labels:
        d = c.replace("_", " ").lower().strip()
        if d.startswith(fr + " "):
            d = d[len(fr) + 1:]
        if d.endswith(" " + fr):
            d = d[: -len(fr) - 1]
        out[d] = c
    return out


def _emb(x):
    """transformers 4.x/5.x return either a tensor or an output object."""
    for attr in ("image_embeds", "text_embeds", "pooler_output"):
        if hasattr(x, attr):
            return getattr(x, attr)
    return x


def _p(cfg):
    rid = hashlib.sha1(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16]
    return RESULTS / (cfg["exp"] + "__" + cfg["dataset"].replace("/", "_") + "__" + rid + ".json")


def save(cfg, met, extra=None):
    p = _p(cfg)
    rec = {"config": cfg, "metrics": met, "code_version": CODE_VERSION,
           "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S"), "extra": extra or {}}
    atomic_write_json(p, rec)
    return rec


# ------------------------------------------------------------------ CLIP
CLIP_TEMPLATES = [
    "a photo of {art} {c} {fruit}",
    "a close-up photo of {art} {c} {fruit}",
    "a {fruit} that is {c}",
]


def clip_zeroshot(ds, view, fruit, ordinal, templates=CLIP_TEMPLATES,
                  model_dir="/model/HuggingFace/openai/clip-vit-large-patch14", max_n=400):
    import torch
    from transformers import CLIPModel, CLIPProcessor
    from PIL import Image
    cfg = {"exp": "B1_clip_zeroshot", "dataset": ds, "view": view,
           "encoder": "clip-vit-large-patch14", "variant": "text", "head": "zero-shot",
           "shot": 0, "seed": 0, "C": None, "control": "none"}
    if _p(cfg).exists():
        return read_json(_p(cfg))
    m = _meta(ds)
    labels = [c for c in ordinal if c in set(m["label_name"])]
    # Restrict to THIS view's classes BEFORE capping. `_cap` samples per label_name, so
    # handing it the whole test split of a multi-fruit dataset let the other fruits'
    # classes through: field4_banana's 120-sample budget became 240 rows, half of them
    # mango, and those rows were then scored as errors against a 2-class label set.
    te = m[(m["split"] == "test") & m["label_name"].isin(labels)]
    te = _cap(te, labels, max_n)
    assert set(te["label_name"]) <= set(labels), "test split leaked classes outside the view"
    model = CLIPModel.from_pretrained(model_dir, local_files_only=True).cuda().eval()
    proc = CLIPProcessor.from_pretrained(model_dir, local_files_only=True)
    with torch.no_grad():
        imgs = [Image.open(q).convert("RGB") for q in _paths(te)]
        inp = proc(images=imgs, return_tensors="pt", padding=True)
        inp = {k: v.cuda() for k, v in inp.items()}
        img_emb = _emb(model.get_image_features(**inp))
        img_emb = img_emb / img_emb.norm(dim=-1, keepdim=True)
        txt, disp = [], display_names(labels, fruit)
        for cs in disp:
            art = "an" if cs[0] in "aeiou" else "a"
            texts = [t.format(c=cs, fruit=fruit, art=art) for t in templates]
            ti = proc(text=texts, return_tensors="pt", padding=True)
            ti = {k: v.cuda() for k, v in ti.items()}
            e = _emb(model.get_text_features(**ti))
            e = e / e.norm(dim=-1, keepdim=True)
            txt.append(e.mean(0))
        T = torch.stack(txt)
        T = T / T.norm(dim=-1, keepdim=True)
        sims = (img_emb @ T.T).cpu().numpy()
    order = list(disp.values())
    pred = np.array([order[i] for i in sims.argmax(1)])
    met = closed_set_metrics(te["label_name"].values, pred, labels)
    met.update({"n_test": int(len(te)), "test_ids_sha256": sha256_ids(te["id"].values),
                "prompt_templates": templates, "class_prompts": list(disp.keys())})
    del model
    torch.cuda.empty_cache()
    return save(cfg, met)


# ------------------------------------------------------------------ Qwen2-VL
_QWEN = {}


def _qwen_load(model_dir, quant="bf16"):
    """Load once per process and reuse.

    Reloading for every (view, shot) pair was the cause of a hard OOM: the old copy
    was not fully released (torch reported ~19 GB still allocated right after a
    `del model; empty_cache()`), so the third or fourth view in a row died with
    "tried to allocate 5.19 GiB ... 4.00 GiB free". One model per process keeps the
    footprint flat at roughly the weight size plus the activations of one call.
    """
    import torch
    key = (str(model_dir), quant)
    if key in _QWEN:
        return _QWEN[key]
    from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
    kw = dict(torch_dtype=torch.bfloat16, device_map="cuda")
    if quant == "4bit":
        from transformers import BitsAndBytesConfig
        kw = dict(quantization_config=BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16), device_map="cuda")
    model = Qwen2VLForConditionalGeneration.from_pretrained(model_dir, **kw).eval()
    proc = AutoProcessor.from_pretrained(model_dir, min_pixels=256 * 28 * 28, max_pixels=768 * 28 * 28)
    _QWEN[key] = (model, proc)
    return model, proc


def _qwen_chat(model, proc, content, max_new=16):
    import torch
    from qwen_vl_utils import process_vision_info
    msgs = [{"role": "user", "content": content}]
    text = proc.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(msgs)
    inputs = proc(text=[text], images=image_inputs, videos=video_inputs,
                  padding=True, return_tensors="pt").to("cuda")
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_new, do_sample=False)
    trimmed = out[:, inputs.input_ids.shape[1]:]
    return proc.batch_decode(trimmed, skip_special_tokens=True)[0].strip()


def parse_label(text, labels):
    t = " " + text.lower() + " "
    for c in sorted(labels, key=len, reverse=True):  # "overripe" before "ripe"
        if re.search(r"\b" + re.escape(c.replace("_", " ").lower()) + r"\b", t):
            return c
    return None


def qwen_eval(ds, view, fruit, ordinal, shot=0, model_dir="/root/rio/models/Qwen2-VL-7B-Instruct",
              quant="bf16", max_n=180, seed=0):
    import torch
    cfg = {"exp": "B2_qwen_%s" % ("zeroshot" if shot == 0 else "%dshot" % shot), "dataset": ds,
           "view": view, "encoder": "Qwen2-VL-7B-Instruct", "variant": quant, "head": "in-context",
           "shot": shot, "seed": seed, "C": None, "control": "none"}
    if _p(cfg).exists():
        return read_json(_p(cfg))
    m = _meta(ds)
    labels = [c for c in ordinal if c in set(m["label_name"])]
    # same reason as in clip_zeroshot: filter to the view's classes before capping
    te = m[(m["split"] == "test") & m["label_name"].isin(labels)]
    te = _cap(te, labels, max_n, seed)
    assert set(te["label_name"]) <= set(labels), "test split leaked classes outside the view"
    pool = m[m["split"] == "train"]
    ex = []
    if shot > 0:
        for c in labels:
            cand = pool[pool["label_name"] == c]
            take = cand.sample(min(shot, len(cand)), random_state=seed)
            ex.append((c, _paths(take)))
    model, proc = _qwen_load(model_dir, quant)
    # `disp` maps display name -> internal class name ("raw" -> "Raw_Banana").
    # Parsing looks up by display name; prompt text needs the reverse direction.
    disp = display_names(labels, fruit)
    back = dict(disp)                             # display -> internal (lookup after parsing)
    fwd = {c: d for d, c in disp.items()}         # internal -> display (used in prompts)
    cls_str = ", ".join(disp.keys())
    preds, answers = [], []
    t0 = time.time()
    for k, (_, r) in enumerate(te.iterrows()):
        content = []
        if shot > 0:
            content.append({"type": "text", "text": "Examples of %s ripeness classes (%s). Each image is followed by its class.\n" % (fruit, cls_str)})
            for c, ps in ex:
                for q in ps:
                    content.append({"type": "image", "image": q})
                    # The exemplar must be labelled with the SAME vocabulary the answer
                    # options use. Labelling it with the internal class name ("Raw_Banana")
                    # while the options are ("raw", "ripe") made the model copy the
                    # exemplar verbatim; every field4 5-shot answer came back as
                    # "Raw_Banana", which is not an option, so it was scored as
                    # __unparsed__ and the view reported acc=0.000. That number was a
                    # prompt-vocabulary mismatch, not a model limitation.
                    content.append({"type": "text", "text": "This is %s.\n" % fwd[c]})
            content.append({"type": "image", "image": str(PROC / r["path"])})
            content.append({"type": "text", "text": "Classify the LAST image. Answer with exactly one class name from: %s." % cls_str})
        else:
            content.append({"type": "image", "image": str(PROC / r["path"])})
            content.append({"type": "text", "text": "Classify the ripeness stage of the %s in this image into exactly one of: %s. Answer with exactly one class name, nothing else." % (fruit, cls_str)})
        try:
            ans = _qwen_chat(model, proc, content)
        except Exception as e:
            log("[qwen] error %s: %s" % (r["id"], e))
            ans = ""
        lab = parse_label(ans, list(disp.keys()))
        answers.append(ans)
        preds.append(back[lab] if lab is not None else "__unparsed__")
        if k % 25 == 0:
            log("[qwen] %s %s %d/%d %.1fs" % (ds, view, k, len(te), time.time() - t0))
        if k % 50 == 49:
            # release the per-call activation blocks so the footprint does not creep
            del content
            import gc
            gc.collect()
            torch.cuda.empty_cache()
    preds = np.array(preds)
    met = closed_set_metrics(te["label_name"].values, preds, labels)
    met.update({"unparsed_rate": float((preds == "__unparsed__").mean()),
                "n_test": int(len(te)), "test_ids_sha256": sha256_ids(te["id"].values),
                "raw_answer_examples": answers[:20]})
    import gc
    gc.collect()
    torch.cuda.empty_cache()   # the model is cached in _QWEN; never reload it per view
    return save(cfg, met)

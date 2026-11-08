#!/bin/bash
# Keep the pipeline driver alive.
#
# There is no cron and no systemd in this container, so if master2.sh ever EXITS (OOM
# killer, a shell-level error, the container sending a signal) nothing would restart it
# and the author is away. The per-stage `timeout` guard only covers a HUNG stage; this
# covers a DEAD driver.
#
# Rules:
#   * STOP file present -> do nothing (an explicit stop must stay stopped);
#   * a driver is running -> do nothing;
#   * otherwise start one, exactly the way START.sh does.
# Idempotent by construction: it only ever starts the driver when `pgrep` finds none.
cd "$(cd "$(dirname "$0")" && pwd)" || exit 1
while true; do
  if [ ! -f STOP ]; then
    if ! pgrep -f 'maste[r]2.sh' >/dev/null 2>&1; then
      echo "[watchdog] driver absent, starting $(date -Is)" >> logs/watchdog.log
      setsid nohup bash master2.sh >> logs/master.out 2>&1 < /dev/null &
      sleep 5
    fi
  fi
  sleep 300
done

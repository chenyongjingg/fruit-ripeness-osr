#!/bin/bash
# Restart the unattended pipeline. Safe any time: every stage is idempotent.
# Also (re)starts the watchdog, which brings the driver back if it ever dies.
cd /root/rio || exit 1
rm -f STOP
if ! pgrep -f 'watchdo[g].sh' >/dev/null 2>&1; then
  setsid nohup bash watchdog.sh >> logs/watchdog.out 2>&1 < /dev/null &
  sleep 1
fi
if pgrep -f 'maste[r]2.sh' >/dev/null 2>&1; then echo already_running; exit 0; fi
setsid nohup bash master2.sh >> logs/master.out 2>&1 < /dev/null &
sleep 2
pgrep -af 'maste[r]2.sh'
pgrep -af 'watchdo[g].sh'

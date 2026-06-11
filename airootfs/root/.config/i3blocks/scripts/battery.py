#!/usr/bin/env python3
import os
import subprocess

if os.environ.get("BLOCK_BUTTON"):
    subprocess.run(["pkill", "-RTMIN+10", "i3blocks"])

battery_path = "/sys/class/power_supply/BAT0"
ac_path = "/sys/class/power_supply/AC"

with open(f"{battery_path}/capacity") as f:
    pct = int(f.read().strip())

with open(f"{ac_path}/online") as f:
    ac = int(f.read().strip())

if ac:
    print(f"BAT: {pct}%")
    print()
    print("#00FF00")
else:
    try:
        with open(f"{battery_path}/charge_now") as f:
            charge_now = int(f.read().strip())
        with open(f"{battery_path}/current_now") as f:
            current_now = int(f.read().strip())
        hours = charge_now / current_now
        h = int(hours)
        m = int((hours - h) * 60)
        time_str = f" ({h}h{m:02d}m)"
    except (FileNotFoundError, ZeroDivisionError):
        time_str = ""

    print(f"BAT: {pct}%{time_str}")
    print()
    print("#FF0000" if pct <= 25 else "#FF8800")

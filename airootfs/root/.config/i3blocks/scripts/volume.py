#!/usr/bin/env python3
import os
import subprocess

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()

if os.environ.get("BLOCK_BUTTON") == "1":
    result = subprocess.run(["pgrep", "-x", "pulsemixer"], capture_output=True)
    if result.returncode == 0:
        subprocess.run(["pkill", "-x", "pulsemixer"])
    else:
        subprocess.Popen(["alacritty", "--title", "pulsemixer", "-e", "pulsemixer"])

mute = run(["pactl", "get-sink-mute", "@DEFAULT_SINK@"])
vol = run(["pactl", "get-sink-volume", "@DEFAULT_SINK@"])
mic_mute = run(["pactl", "get-source-mute", "@DEFAULT_SOURCE@"])
mic_vol = run(["pactl", "get-source-volume", "@DEFAULT_SOURCE@"])

is_muted = "yes" in mute
is_mic_muted = "yes" in mic_mute

def parse_percent(s):
    for token in s.split():
        if token.endswith("%"):
            return token.strip("%")
    return "?"

percent = parse_percent(vol)
mic_percent = parse_percent(mic_vol)

out = "muted" if is_muted else f"{percent}%"
mic_out = "muted" if is_mic_muted else f"{mic_percent}%"

print(f"  IN: {mic_out}  |   VOL: {out}   ")
print()
if is_muted:
    print("#FF0000")
else:
    print("#00FF00")

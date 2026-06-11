#!/usr/bin/env python3
import os
import subprocess

TOGGLE_FILE = "/tmp/i3blocks_network_hide_ip"

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()

button = os.environ.get("BLOCK_BUTTON")
if button == "1":
    subprocess.Popen(["ronema"])
elif button == "3":
    if os.path.exists(TOGGLE_FILE):
        os.remove(TOGGLE_FILE)
    else:
        open(TOGGLE_FILE, "w").close()

hide_ip = not os.path.exists(TOGGLE_FILE)

essid = run(["iwgetid", "-r"])
ip_out = run(["ip", "route", "get", "1.1.1.1"])
ping_out = run(["ping", "-c", "1", "-W", "1", "1.1.1.1"])

ip = None
for token in ip_out.split():
    if token == "src":
        ip = ip_out.split()[ip_out.split().index("src") + 1]
        break

if not ip:
    print("  NET: down  ")
    print()
    print("#FF0000")
    exit()

def censor_ip(ip):
    parts = ip.split(".")
    return f"{parts[0]}.{'***'}.{'**'}.{parts[3]}"

ip_display = censor_ip(ip) if hide_ip else ip

ping = None
for line in ping_out.splitlines():
    if "time=" in line:
        ping = float(line.split("time=")[1].split()[0])
        break

ping_str = f"{ping:.0f}ms" if ping is not None else "timeout"

if essid:
    print(f"  WiFi: {essid}  {ip_display}  {ping_str}  ")
else:
    print(f"  Ethernet  {ip_display}  {ping_str}  ")

print()
if ping is None:
    print("#FF0000")
elif ping > 100:
    print("#FF8800")
else:
    print("#00FF00")

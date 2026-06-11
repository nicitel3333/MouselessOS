#!/usr/bin/env python3
import subprocess

result = subprocess.run(["ip", "-6", "addr", "show", "scope", "global"], capture_output=True, text=True)

ipv6 = None
for line in result.stdout.splitlines():
    if "inet6" in line:
        ipv6 = line.split()[1]
        break

if ipv6:
    print(f"   IPv6: {ipv6}   ")
    print()
    print("#00FF00")
else:
    print("   IPv6: none   ")
    print()
    print("#FF0000")

#!/usr/bin/env python3
import time

def read_cpu():
    with open("/proc/stat") as f:
        fields = list(map(int, f.readline().split()[1:]))
    idle = fields[3]
    total = sum(fields)
    return idle, total

idle1, total1 = read_cpu()
time.sleep(0.5)
idle2, total2 = read_cpu()

pct = int((1 - (idle2 - idle1) / (total2 - total1)) * 100)

print(f"   CPU: {pct}%   ")
print()
if pct >= 90:
    print("#FF0000")
elif pct >= 50:
    print("#FF8800")
else:
    print("#00FF00")

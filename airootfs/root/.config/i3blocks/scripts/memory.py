#!/usr/bin/env python3

with open("/proc/meminfo") as f:
    info = {}
    for line in f:
        key, val = line.split()[0].rstrip(":"), int(line.split()[1])
        info[key] = val

total = info["MemTotal"] // 1024
used = total - (info["MemFree"] + info["Buffers"] + info["Cached"] + info["SReclaimable"]) // 1024
pct = used * 100 // total
used_g = used / 1024
total_g = total / 1024

print(f"   RAM: {used_g:.1f}G   ")
print()

if pct >= 85:
    print("#FF0000")
elif pct >= 70:
    print("#FF8800")
else:
    print("#00FF00")

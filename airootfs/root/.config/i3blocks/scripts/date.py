#!/usr/bin/env python3
import os
import subprocess
if os.environ.get("BLOCK_BUTTON") == "1":
    result = subprocess.run(["pgrep", "gsimplecal"], capture_output=True)
    if result.returncode == 0:
        subprocess.run(["pkill", "gsimplecal"])
    else:
        subprocess.Popen(["gsimplecal"])
from datetime import datetime
print(f"  {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}  ")
print()
print("#00FF00")

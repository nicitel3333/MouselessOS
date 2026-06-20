#!/usr/bin/env python3
import os
import subprocess
if os.environ.get("BLOCK_BUTTON") == "1":
    subprocess.Popen(["alacritty", "-e", "tdl"])
from datetime import datetime
print(f"  {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}  ")
print()
print("#00FF00")

#!/usr/bin/env bash
# shellcheck disable=SC2034
iso_name="mouselessos"
iso_label="MOUSELESSOS_$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y%m)"
iso_publisher="nicitel3333"
iso_application="MouselessOS"
iso_version="$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux'
           'uefi.systemd-boot')
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'zstd' '-Xcompression-level' '15')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/root"]="0:0:750"
  ["/root/.config/i3blocks/scripts/battery.py"]="0:0:755"
  ["/root/.config/i3blocks/scripts/date.py"]="0:0:755"
  ["/root/.config/i3blocks/scripts/memory.py"]="0:0:755"
  ["/root/.config/i3blocks/scripts/volume.py"]="0:0:755"
  ["/root/.config/i3blocks/scripts/cpu.py"]="0:0:755"
  ["/root/.config/i3blocks/scripts/ipv6.py"]="0:0:755"
  ["/root/.config/i3blocks/scripts/network.py"]="0:0:755"
)

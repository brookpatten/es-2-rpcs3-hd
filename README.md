# es-2-rpcs3-hd
## Add your *installed* ps3 roms to Emulation station
### Default values are for steamdeck with emudeck installed to SD, but you can change the paths to what suits you

This script creates symlinks so that your games installed into your rcps3 "hard drive" will show in emulation station.

Assumes your installed ps3 games are in /run/media/mmcblk0p1/Emulation/storage/rpcs3/dev_hdd0/game
Assumes your Roms folder is /run/media/mmcblk0p1/Emulation/roms

1) Download files
2) chmod +x esps3.sh
3) ./esps3.sh

This will create links in /run/media/mmcblk0p1/Emulation/roms/ps3/<game title>

You will still need to edit ~/.emulationstation/custom_systems/es_systems.xml to add ps3.  
See es-ps3-custom-system.xml as an example of what to add to the systems element
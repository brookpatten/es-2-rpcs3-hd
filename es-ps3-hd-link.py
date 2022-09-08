import os
from ps3iso.sfo import SfoFile

#locate hd dir
ps3HdDir = "/run/media/mmcblk0p1/Emulation/storage/rpcs3/dev_hdd0/game"

if not os.path.exists(ps3HdDir):
  print("couldn't find ps3 hd, please edit the script to add the correct path")
  quit()

#locate rom dir
romsDir = "/run/media/mmcblk0p1/Emulation/roms/ps3"

if not os.path.exists(romsDir):
  print("couldn't find ps3 roms dir, please edit the script to add the correct path")
  quit()

#loop through hd dir
for dir in os.listdir(ps3HdDir):
  print('checking '+dir)
  #only check it if it's a directory
  if os.path.isdir(ps3HdDir+'/'+dir):
    #only check it if it contains param.sfo
    if os.path.exists(ps3HdDir+'/'+dir + '/PARAM.SFO'):
      #only check it if it has an eboot.bin to run
      if os.path.exists(ps3HdDir+'/'+dir+"/USRDIR/EBOOT.BIN") or os.path.exists(ps3HdDir+'/'+dir+"/USRDIR/ISO.BIN.EDAT"):
        #parse title
        sfo = SfoFile.parse_file(ps3HdDir+'/'+dir+'/PARAM.SFO')
        #clean/trim title
        title = sfo.parameters.TITLE
        title = ''.join(e for e in title if e.isalnum() or e==' ')
        print(dir+" is "+title)
        if not os.path.exists(romsDir+'/'+title):
          #symlink named title to hd dir
          os.symlink(ps3HdDir+'/'+dir,romsDir+'/'+title)
          print("linked "+romsDir+'/'+title+" to "+ps3HdDir+'/'+dir)
        else:
          print(romsDir+'/'+title+' already exists')
      else:
        print('missing '+dir+'/USRDIR/EBOOT.BIN')
    else:
      print('missing '+'/PARAM.SFO')
  else:
    print ("not a directory")

print("In order for ps3 to show in emulation station you will also need to edit ~/.emulationstation/custom_systems/es_systems.xml")
print("use es-ps3-custom-system.xml as an example")

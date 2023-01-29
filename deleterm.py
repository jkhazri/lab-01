import os


outpath= '/home/youffes/cdrxl/'
basepath = '/home/youffes/cdr/'
with os.scandir(basepath) as entries:
 for entry in entries:
   path=(basepath+entry.name)
   os.remove(path)
with os.scandir(outpath) as entries:
 for entry in entries:
   path=(basepath+entry.name)
   os.remove(path)
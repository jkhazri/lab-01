import os
import pandas as pd

# List all files in a directory using scandir()
basepath = '/home/youffes/cdr/'
outpath= '/home/youffes/cdrxl/'
with os.scandir(basepath) as entries:
    for entry in entries:
     path=(basepath+entry.name)
     pathout=(outpath+entry.name)
     #print(pathout)
     df = pd.read_csv(path, delimiter=',')
     df.to_csv(pathout+'.csv', index=None ,encoding='utf-8-sig')

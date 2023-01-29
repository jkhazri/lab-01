import os
import glob
import pandas as pd
from os import path
os.chdir("/home/youffes/cdrxl/")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
i=0
while path.exists("/home/youffes/logdeck/result"+str(i)+".csv"):
    i+=1
combined_csv.to_csv( "/home/youffes/logdeck/result"+str(i)+".csv", index=None )
   
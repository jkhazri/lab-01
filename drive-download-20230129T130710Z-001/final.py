import os
import pandas as pd
import glob
from os import path
import schedule
import time
import csv
import psycopg2.extras
import psycopg2
from datetime import datetime

def main():
    #format cdr files
    basepath = '/home/youffes/cdr/'
    with os.scandir(basepath) as entries:
     for entry in entries:
      pathn=(basepath+entry.name)
      with open(pathn, "r") as f:
       lines = f.readlines()
      with open(pathn, "w") as f:
       for line in lines:
        if (line.strip("\n") !=  "INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(50),VARCHAR(128),INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(64),VARCHAR(64),INTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(50),VARCHAR(50),VARCHAR(128),INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(64),VARCHAR(64),INTEGER,INTEGER,VARCHAR(50),UNIQUEIDENTIFIER,VARCHAR(50),VARCHAR(50),VARCHAR(50),VARCHAR(50),INTEGER,VARCHAR(129),VARCHAR(129),INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(50),INTEGER,VARCHAR(2048),VARCHAR(50),INTEGER,VARCHAR(32),INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(32),VARCHAR(50),VARCHAR(50),VARCHAR(64),VARCHAR(64),INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(32),INTEGER,VARCHAR(32),INTEGER,INTEGER,INTEGER,VARCHAR(50),VARCHAR(50),INTEGER,VARCHAR(50),VARCHAR(50),VARCHAR(50),VARCHAR(50),VARCHAR(50),VARCHAR(50),VARCHAR(50),VARCHAR(50),INTEGER,INTEGER,VARCHAR(255),VARCHAR(255),VARCHAR(255),VARCHAR(255),VARCHAR(50),VARCHAR(50),VARCHAR(129),VARCHAR(129),INTEGER,INTEGER,INTEGER,VARCHAR(50),VARCHAR(50),VARCHAR(50),VARCHAR(50)")  :
            f.write(line) 
           
  
    #transform cdr to csv 
    basepath = '/home/youffes/cdr/'
    outpath= '/home/youffes/cdrxl/'
    with os.scandir(basepath) as entries:
      for entry in entries:
        pathin=(basepath+entry.name)
        pathout=(outpath+entry.name)
        df = pd.read_csv(pathin, delimiter=',')
        df.to_csv(pathout+'.csv', index=None ,encoding='utf-8-sig')
    

    #regroup into one csv
    os.chdir("/home/youffes/cdrxl/")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( "/home/youffes/cdrxl/result.csv", index=None )
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    a = f"result_{date}" 
    combined_csv.to_csv("/home/youffes/logdeck/log"+a+".csv", index=None )
     
    #connect and insert 
    DB_HOST = "ubuntu"
    DB_NAME = "postgres"
    DB_USER = "postgres"
    DB_PASS = "admin"
    
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()

    with open('/home/youffes/cdrxl/result.csv', 'r') as f:
      next(f) # Skip the header row
      cur.copy_from(f, 'result', sep=',', null ='')
    conn.commit()
    cur.execute('INSERT INTO taxet ("pkid", "dateTimeOrigination", "callingPartyNumber", "finalCalledPartyNumber", "duration" ) SELECT  "pkid", "dateTimeOrigination", "callingPartyNumber", "finalCalledPartyNumber", "duration" FROM result;')
    conn.commit()
    cur.execute('delete from result;')
    conn.commit()
    cur.close()
    conn.close()
    

    #delete old files
    outpath= '/home/youffes/cdrxl/'
    basepath = '/home/youffes/cdr/'
    with os.scandir(basepath) as entries:
     for entry in entries:
      pathto=(basepath+entry.name)
      os.remove(pathto)
    with os.scandir(outpath) as entries:
     for entry in entries:
      pathtoo=(outpath+entry.name)
      os.remove(pathtoo)
    
    import parite2
    
    print("done")

schedule.every(4).seconds.do(main)
   
while 1:
   if len(os.listdir('/home/youffes/cdr') ) == 0:
    print("Directory is empty")
   else:    
    schedule.run_pending()
    time.sleep(1)
    
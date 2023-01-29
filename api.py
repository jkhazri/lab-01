import psycopg2.extras
import psycopg2
import sys
import psycopg2.extras
from datetime import datetime
import schedule
import time
import os

DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"
 
# make connection between python and postgresql
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

que = ('select "callingPartyNumber","price" from reportingf where "price" = 30;')
cur.execute(que)
table = cur.fetchall()
info = []
for row in table:
   info.append(row[0])
date = datetime.now().strftime("%Y_%m_%d")
a = f"rapport_{date}"
outF = open("/home/youffes/logdeck/rapport/"+a + ".txt", "w")
for line in info:
   outF.write(line)
   outF.write("\n")
outF.close()
filesize = os.path.getsize("/home/youffes/logdeck/rapport/"+a + ".txt")
if filesize == 0:
   next
else:
   import apiv1
   import quota
    
 
print("done")


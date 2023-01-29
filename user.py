DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"

import csv
import psycopg2.extras
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

#with open('/home/youffes/logdeck/result6.csv', 'r') as f:
#next(f) # Skip the header row
#cur.copy_from(f, 'result', sep=',', null ='')


#create user database
for i in range(1, 128):
 que=('create table userf'+str(i)+' ("dateTimeOrigination" INT, "duration" INT,"price" float8 );')
 
 cur.execute(que)
 conn.commit()
cur.close()
conn.close()

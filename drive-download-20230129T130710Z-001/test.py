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
import sys
import psycopg2
import csv 
import pandas as pd

DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"

#make connection between python and postgresql
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

que=('INSERT INTO taxationnatr ("pkid", "date", "callingPartyNumber", "finalCalledPartyNumber", "duration", "price") SELECT * FROM taxationft WHERE "finalCalledPartyNumber"  like %s ;')
args=['94%']
cur.execute(que,args)
conn.commit()

que=('INSERT INTO taxationnatr ("pkid", "date", "callingPartyNumber", "finalCalledPartyNumber", "duration", "price") SELECT * FROM taxationft WHERE "finalCalledPartyNumber"  like %s ;')
args=['95']
cur.execute(que,args)
conn.commit()

que=('INSERT INTO taxationnatr ("pkid", "date", "callingPartyNumber", "finalCalledPartyNumber", "duration", "price") SELECT * FROM taxationft WHERE "finalCalledPartyNumber"  like %s ;')
args=['97%']
cur.execute(que,args)
conn.commit()

que=('INSERT INTO taxationnatr ("pkid", "date", "callingPartyNumber", "finalCalledPartyNumber", "duration", "price") SELECT * FROM taxationft WHERE "finalCalledPartyNumber"  like %s ;')
args=['99%']
cur.execute(que,args)
conn.commit()

que=('INSERT INTO taxationnat ("pkid", "date", "callingPartyNumber", "finalCalledPartyNumber", "duration", "price") SELECT * FROM taxationnatr;')
cur.execute(que)
conn.commit()

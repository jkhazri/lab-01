import psycopg2
import csv 
DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

que=('INSERT INTO taxationtotal ("pkid", "date", "callingPartyNumber", "finalCalledPartyNumber", "duration", "price") SELECT * FROM taxationnatr;')
cur.execute(que)
conn.commit()

sql2=('INSERT INTO taxationtotal ("pkid", "date","callingPartyNumber", "finalCalledPartyNumber", "duration" ,"price") SELECT * FROM taxationinterft ;')
cur.execute(sql2)
conn.commit()
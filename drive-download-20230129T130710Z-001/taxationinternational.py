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

sql = "COPY (SELECT * FROM taxationintert ) TO STDOUT WITH CSV DELIMITER ',' HEADER ;"
with open("/home/youffes/finaly/taxationintert.csv", "w") as file:
    cur.copy_expert(sql, file)


cotation = 1
df = pd.read_csv("/home/youffes/finaly/taxationintert.csv")
df['price'] = df.apply (lambda row: ((row['duration'])/60)*cotation, axis=1)
df.to_csv("/home/youffes/finaly/taxationinterft.csv", index=False)

with open('/home/youffes/finaly/taxationinterft.csv', 'r') as f:
      next(f) 
      cur.copy_from(f, 'taxationinterft', sep=',', null ='')
      conn.commit()


sql2=('INSERT INTO taxationinterf ("pkid", "date","callingPartyNumber", "finalCalledPartyNumber", "duration" ,"price") SELECT * FROM taxationinterft ;')
cur.execute(sql2)
conn.commit()



conn.close()
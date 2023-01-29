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

sql = "COPY (SELECT * FROM taxationt ) TO STDOUT WITH CSV DELIMITER ',' HEADER ;"
with open("/home/youffes/finaly/taxationt.csv", "w") as file:
    cur.copy_expert(sql, file)


cotation = 0.6
df = pd.read_csv("/home/youffes/finaly/taxationt.csv")
df['price'] = df.apply (lambda row: ((row['duration'])/60)*cotation, axis=1)
df.to_csv("/home/youffes/finaly/taxationft.csv", index=False)

with open('/home/youffes/finaly/taxationft.csv', 'r') as f:
      next(f) 
      cur.copy_from(f, 'taxationft', sep=',', null ='')
      conn.commit()



conn.close()
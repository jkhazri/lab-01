import sys
import psycopg2
import csv 
DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"

#make connection between python and postgresql
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()
for i in range(1, 128):
 a="user"+str(i)
 output="/home/youffes/tax/"+a+".csv"
 sql = "COPY (SELECT * FROM "+a+") TO STDOUT WITH CSV DELIMITER ',' HEADER ;"
 with open(output, "w") as file:
     cur.copy_expert(sql, file)

conn.close()
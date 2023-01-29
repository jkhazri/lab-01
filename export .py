import sys

#set up psycopg2 environment
import psycopg2
import csv 
DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"

#make connection between python and postgresql
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

sql = "COPY (SELECT * FROM taxet) TO STDOUT WITH CSV DELIMITER ',' HEADER ;"
with open("/home/youffes/code/table.csv", "w") as file:
    cur.copy_expert(sql, file)

conn.close()
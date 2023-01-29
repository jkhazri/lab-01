import csv
import psycopg2.extras
import psycopg2
from psycopg2 import sql

DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()


with open('/home/youffes/outputfile.csv', 'r') as f:
      next(f) # Skip the header row
      cur.copy_from(f, 'taxes', sep=',', null ='')
      conn.commit()
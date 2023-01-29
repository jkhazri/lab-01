import os
import pandas as pd
import glob
from os import path
import schedule
import time
import csv
import psycopg2.extras
import psycopg2
import sys

DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

custom_date_parser = lambda x: pd.to_datetime(x,unit= 's')
df = pd.read_csv('/home/youffes/finaly/outputfile.csv',
                 parse_dates=['dateTimeOrigination'],
                 date_parser=custom_date_parser)
df.to_csv("/home/youffes/finaly/output.csv", index=False)
df = pd.read_csv('/home/youffes/finaly/output.csv')
df['dateTimeOrigination'] = pd.to_datetime(df['dateTimeOrigination']).dt.floor('d')
df.to_csv("/home/youffes/finaly/output2.csv", index=False)

with open('/home/youffes/finaly/output2.csv', 'r') as f:
      next(f) # Skip the header row
      cur.copy_from(f, 'taxest', sep=',', null ='')
      conn.commit()

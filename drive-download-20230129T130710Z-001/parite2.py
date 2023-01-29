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

#make connection between python and postgresql
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

sql = "COPY (SELECT * FROM taxet) TO STDOUT WITH CSV DELIMITER ',' HEADER ;"
with open("/home/youffes/finaly/table.csv", "w") as file:
    cur.copy_expert(sql, file)


import mold

import timemod

import taxationinterne

import taxationexterne

import international

import taxationtotal

import taxationnat

import taxationinternational

import taxationfinal

import notification

import api

cur.execute('DELETE from transit;')
conn.commit()

cur.execute('DELETE from taxationlt;')
conn.commit()

cur.execute('DELETE from taxationt;')
conn.commit()

cur.execute('DELETE from taxationft;')
conn.commit()

cur.execute('DELETE from taxationintert;')
conn.commit()

cur.execute('DELETE from taxationinterft;')
conn.commit()

cur.execute('DELETE from taxationnatr;')
conn.commit()

cur.execute('DELETE from taxest;')
conn.commit()

cur.execute('DELETE from taxet;')
conn.commit()

cur.execute('DELETE from reportingft;')
conn.commit()

cur.execute('DELETE from reportingt;')
conn.commit()


conn.close()


basepath = '/home/youffes/finaly/'
with os.scandir(basepath) as entries:
 for entry in entries:
  pathto=(basepath+entry.name)
  os.remove(pathto)
  




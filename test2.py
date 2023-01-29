DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"

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

sql = "COPY (SELECT * FROM taxe) TO STDOUT WITH CSV DELIMITER ',' HEADER ;"
with open("/home/youffes/finaly/table.csv", "w") as file:
    cur.copy_expert(sql, file)

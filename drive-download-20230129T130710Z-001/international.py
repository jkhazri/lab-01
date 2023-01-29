import psycopg2.extras
import psycopg2


DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"



conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()


que=('INSERT INTO taxationintert ("pkid", "date", "callingPartyNumber", "finalCalledPartyNumber", "duration") SELECT * FROM taxationt WHERE "finalCalledPartyNumber"  like %s ;')
args=['900%']
cur.execute(que,args)
conn.commit()


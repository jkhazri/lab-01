import psycopg2.extras
import psycopg2


DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()


sql1=('INSERT INTO transit ("pkid", "date", "callingPartyNumber", "finalCalledPartyNumber", "duration") SELECT * FROM taxest WHERE "callingPartyNumber"  ~ %s;')
args=['^[A-Z].*']
cur.execute(sql1,args)
conn.commit()

sql3=('INSERT INTO taxationlt ("pkid", "date","callingPartyNumber", "finalCalledPartyNumber", "duration") SELECT * FROM transit WHERE "finalCalledPartyNumber" ~ %s;')
args=['^[A-Z].*']
cur.execute(sql3,args)
conn.commit()

sql2=('INSERT INTO taxationl ("pkid", "date","callingPartyNumber", "finalCalledPartyNumber", "duration") SELECT * FROM taxationlt ;')
cur.execute(sql2)
conn.commit()







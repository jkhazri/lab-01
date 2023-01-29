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



que=('insert into reportingft ("date","callingPartyNumber","price") SELECT  "date","callingPartyNumber", "price" FROM taxationtotal WHERE EXTRACT(Year FROM date) = (SELECT date_part(%s , (SELECT current_timestamp)));')
args=['Year']
cur.execute(que,args)
conn.commit()

que=('insert into reportingt ("callingPartyNumber","price") select "callingPartyNumber","price" from reportingft WHERE EXTRACT(Month FROM date) = (SELECT date_part(%s , (SELECT current_timestamp)));')
args=['Month']
cur.execute(que,args)
conn.commit()

que=('insert into reporting ("callingPartyNumber","price") select "callingPartyNumber","price" from reportingt ;')
cur.execute(que)
conn.commit()

que=('insert into reportingf ("callingPartyNumber","price") select "callingPartyNumber",count("price") from reporting group by "callingPartyNumber" ;')
cur.execute(que)
conn.commit()

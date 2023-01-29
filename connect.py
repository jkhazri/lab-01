#!/usr/bin/python3
import psycopg2
import csv
import os
import pandas as pd

connection = psycopg2.connect("host='ubuntu' dbname='mydb' user='dbowner' password='MySecretPassword²'")
mycursor = connection.cursor()




def insert_links():
    with open('/home/youffes/combined_csv.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO calldetails (globalCallID_callId,origLegCallIdentifier,dateTimeOrigination,origNodeId,callPartyNumber,callingPartyUnicodeLoginUserID,originalCalledPartyNumber,finalCalledPartyNumber,finalCalledPartyUnicodeLoginUserID,dateTimeConnect,dateTimeDisconnect,lastRedirectDn,pkid,totalWaitTimeInQueue,callingPartyNumber,callingPartyNumberuri,originalCalledPartyNumber_uri,finalCalledPartyNumber_uri,lastRedirectDn_uri) VALUES ('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" 
            print(sql)
            try:
               # Execute the SQL command
               mycursor.execute(sql)
               # Commit your changes in the database
               connection.commit()
            except:
               # Rollback in case there is any error
               connection.rollback()










insert_links()



# disconnect from server
connection.close()
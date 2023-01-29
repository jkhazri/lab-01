from ciscoaxl import axl
import psycopg2.extras
import psycopg2
import sys
import psycopg2.extras
from datetime import datetime
import schedule
import time

from lxml import etree
from requests import Session
from requests.auth import HTTPBasicAuth

from zeep import Client, Settings, Plugin
from zeep.transports import Transport
from zeep.cache import SqliteCache
from zeep.exceptions import Fault
import sys
import urllib3

# Edit .env file to specify your Webex site/user details
import os
from dotenv import load_dotenv
load_dotenv()

DB_HOST = "ubuntu"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()
# The WSDL is a local file
WSDL_FILE = '/home/youffes/code/shema23/AXLAPI.wsdl'


DEBUG = False



cucm = '10.112.22.3'
username = 'axlaccess'
password = 'eWLUSAvV5S2jvn9'
version = '10.5'

# This class lets you view the incoming and outgoing http headers and/or XML
class MyLoggingPlugin( Plugin ):

    def egress( self, envelope, http_headers, operation, binding_options ):

        # Format the request body as pretty printed XML
        xml = etree.tostring( envelope, pretty_print = True, encoding = 'unicode')

        print( f'\nRequest\n-------\nHeaders:\n{http_headers}\n\nBody:\n{xml}' )

    def ingress( self, envelope, http_headers, operation ):

        # Format the response body as pretty printed XML
        xml = etree.tostring( envelope, pretty_print = True, encoding = 'unicode')

        print( f'\nResponse\n-------\nHeaders:\n{http_headers}\n\nBody:\n{xml}' )

session = Session()

# We avoid certificate verification by default, but you can uncomment and set
# your certificate here, and comment out the False setting

#session.verify = CERT
session.verify = False
session.auth = HTTPBasicAuth(username, password )

# Create a Zeep transport and set a reasonable timeout value
transport = Transport( session = session, timeout = 10 )

# strict=False is not always necessary, but it allows zeep to parse imperfect XML
settings = Settings( strict=False, xml_huge_tree=True )

# If debug output is requested, add the MyLoggingPlugin callback
plugin = [ MyLoggingPlugin() ] if DEBUG else [ ]

# Create the Zeep client with the specified settings
client = Client( WSDL_FILE, settings = settings, transport = transport,
        plugins = plugin )

# service = client.create_service("{http://www.cisco.com/AXLAPIService/}AXLAPIBinding", CUCM_URL)
service = client.create_service( '{http://www.cisco.com/AXLAPIService/}AXLAPIBinding',
                                f'https://10.112.22.3:8443/axl/')



username = 'axlaccess'
password = 'eWLUSAvV5S2jvn9'
version = '10.5'

ucm = axl(username=username,password=password,cucm=cucm,cucm_version=version)

que = ('select "callingPartyNumber","price" from reportingf where "price" = 30;')
cur.execute(que)
table = cur.fetchall()
for row in table:
 user=(row[0])
 que = ('select "userid","name" from dict where "name" ~ %s;')
 args=[user+'%']
 cur.execute(que,args)
 tablel =cur.fetchall()
 for row in tablel:
    LINEDN=(row(3))
    USERFNAME=(row(0))
    PHONEID=(row(2))
    phone_data = {
      'name': PHONEID,
      'ownerUserName': USERFNAME,
      'lines': {
          'line': [
              {
                  'index': 1,
                  'dirn': {
                      'pattern': LINEDN,
                      'routePartitionName': None
                 },
                
              }
          ],
      }
    }
    try:
     phone_resp = service.updatePhone(**phone_data)
    except Fault as err:
     print("\nZeep error: {0}".format(err))
    else:
     print("\nupdatePhone response:\n")
     print(phone_resp,"\n")





import pandas as pd
import csv

custom_date_parser = lambda x: pd.to_datetime(x,unit= 's')
df = pd.read_csv('/home/youffes/code/outputfile.csv',
                 parse_dates=['dateTimeOrigination'],
                date_parser=custom_date_parser)
df.to_csv("/home/youffes/finaly/outpute.csv", index=False)

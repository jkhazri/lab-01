import pandas as pd
import csv


df = pd.read_csv('/home/youffes/finaly/outpute.csv')
df['dateTimeOrigination'] = pd.to_datetime(df['dateTimeOrigination']).dt.floor('d')
df.to_csv("/home/youffes/finaly/outpute2.csv", index=False)

import csv
import pdftables_api
conversion = pdftables_api.Client('txs87im48x6l')
conversion.csv('/home/youffes/Downloads/series.pdf', '/home/youffes/Downloads/test.csv')
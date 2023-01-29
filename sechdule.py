import schedule
import time
from datetime import datetime

def main():
    date = datetime.now().strftime("%d")
    if date == str(29):
     import quotaundo
    else:
     next
    print("done")
schedule.every(4).seconds.do(main)
   
while 1:
    schedule.run_pending()
    time.sleep(1)
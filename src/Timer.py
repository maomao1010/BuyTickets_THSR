from datetime import datetime, timedelta
import time

def SetStartingTime(StartingTime):
    StartingTime = datetime.strptime(StartingTime,"%Y/%m/%d %H:%M:%S")
    Current = datetime.now()
    
    while StartingTime > Current:
        Current = datetime.now()
        diff = int((StartingTime - Current).total_seconds())
        if diff > 300:
            print("The program will start after", (diff // 60), "minutes.")
            time.sleep(60)
            
        elif 300 > diff > 60:
            print("The program will start after", (diff // 10) * 10, "seconds.")
            time.sleep(10)
            
        elif diff < 60:
            print("The program will start after", diff, "seconds.")
            time.sleep(1)
            
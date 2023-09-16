import re
from datetime import datetime

def ArgsVerification(args):
    Stations = ["南港","台北","板橋","桃園","新竹","苗栗","台中","彰化","雲林","嘉義","台南","左營"]
    
    if not re.match("[a-zA-z][0-9]{9}", args.id):
        print("The format of your ID is wrong!")
        return False
    
    elif not re.match("yes|Yes|no|No", args.ismember):
        print("Please enter yes/no to the question!")
        return False
    
    elif args.phone != "" and not re.match("[0-9]{10}", args.phone):
        print("The format of your phone is wrong!")
        return False
    
    elif not re.match("1|2", args.trip):
        print("The format of the trip is wrong!")
        return False
    
    elif args.startingstation not in Stations:
        print("The format of the starting station is not exist!")
        return False
    
    elif args.destination not in Stations:
        print("The format of the destination is not exist!")
        return False
    
    try:
        date = datetime.strptime(args.date,"%Y/%m/%d")
        timer = datetime.strptime(args.timer,"%H:%M:%S")
    except:
        print("The format of the start time is wrong!")
        return False
    
    try:
        start = datetime.strptime(args.start,"%Y/%m/%d")
    except:
        print("The format of the start date is wrong!")
        return False
    
    if args.trip == "2":
        if not args.end:
            print("You need to decide when you want to back!")
            return False
        
        if not args.backtrainnumber:
            print("You need to specify the train that you want to back!")
            return False
        
        try:
            end = datetime.strptime(args.end,"%Y/%m/%d")
        except:
            print("The format of the start date is wrong!")
            return False
        
        if end < start:
            print("You can not go back before departure!")
            return False
    
    return True  
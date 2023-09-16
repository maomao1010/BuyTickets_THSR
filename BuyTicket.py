from src.PageOperation import *
from src.Verification import *
from src.Timer import *
import argparse
import sys
import os

UserDatas = {}
TravelDatas = {}

url = "https://irs.thsrc.com.tw/IMINT/"
timeout = 600

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    DefaultStartTime = (datetime.now() + timedelta(days = 1)).strftime("%Y/%m/%d")
    
    parser.add_argument("--id" , type = str, required = True, help = "Please enter your id.")                
    parser.add_argument("--ismember" , type = str, default= "no", help = "Are you the member of THSR? (yes/no)")
    parser.add_argument("--phone" , type = str, default= "", help = "Please enter your phone.")
    parser.add_argument("--email" , type = str, default= "", help = "Please enter your email.")
    parser.add_argument("--key" , type = str, required = True, default= "", help = "Please enter the api key that you get from anticaptcha.")
    
    parser.add_argument("--trip" , type = str, default = "1", help = "1 for one-way and 2 for round-trip ticket.")
    parser.add_argument("--startingstation" , type = str, required = True, help = "Please enter the starting station.")
    parser.add_argument("--destination" , type = str, required = True, help = "Please enter the destination.")
    parser.add_argument("--start" , type = str, required = True, help = "Please enter the date you want to go. (YYYY/MM/DD)")
    parser.add_argument("--end" , type = str, default="", help = "Please enter the date you want to back. (YYYY/MM/DD)")
    parser.add_argument("--totrainnumber" , type = str, required = True, help = "Please enter the train number that you will take to go.")
    parser.add_argument("--backtrainnumber" , type = str, default="", help = "Please enter the train number that you will take to back.")
    parser.add_argument("--tickets" , type = str, default = "1", help = "How many tickets that you want to buy.")
    parser.add_argument("--date" , type = str, default = DefaultStartTime, help = "When would you want to start the program? (YYYY/MM/DD)")
    parser.add_argument("--timer" , type = str, default = "00:00:00", help = "When would you want to start the program? (HH:MM:SS)")
    
    args = parser.parse_args()
    
    if ArgsVerification(args):
        
        #Load datas from command line
        APIKey = args.key

        UserDatas["ID"] = args.id
        UserDatas["IsMember"] = False if (args.ismember == "no" or args.ismember == "No") else True
        UserDatas["Phone"] = args.phone
        UserDatas["Email"] = args.email
        
        TravelDatas["Trip"] = args.trip
        TravelDatas["From"] = args.startingstation
        TravelDatas["To"] = args.destination
        TravelDatas["Start"] = args.start
        TravelDatas["End"] = args.end
        TravelDatas["toTrainNumber"] = args.totrainnumber
        TravelDatas["backTrainNumber"] = args.backtrainnumber
        TravelDatas["Tickets"] = args.tickets
        
        service = Service(executable_path='./driver/chromedriver.exe')
        option = webdriver.ChromeOptions()
        option.add_argument('--profile-directory=Default')
        option.add_argument('--disable-blink-features=AutomationControlled')
        browser = webdriver.Chrome(options=option, service=service)
        SetStartingTime(args.date + " " + args.timer)
        
        #The website may be crowded so we set the maxmium time to {timeout} sec.
        browser.implicitly_wait(timeout)
        browser.get(url)
        CaptchaBox = browser.find_element(By.NAME,"homeCaptcha:securityCode")
        
        #We have success loading the website, so we set the timeout time as 1 sec.
        browser.implicitly_wait(1)
        try:
            cookieAcceptBtn = browser.find_element(By.ID,"cookieAccpetBtn")
            cookieAcceptBtn.click()
        except:
            pass
            
        HomePage(browser, TravelDatas, APIKey)
        ConfirmPage(browser, UserDatas)
        
    else:
        print("Please modify your data and retry.")
    
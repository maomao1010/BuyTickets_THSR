# BuyTickets_THSR
This project can be used to buy THSR tickets automatically. Please use this program carefully because it may be treat as unlegal behavior.

## Getting started
In order to use this program, you have make sure that you have completed the following tasks.

### 1. Install python and the essential environment.
```
pip install -r requirements.txt
```

### 2. Apply for your API to pass the captcha in Anticaptcha.

Anticaptcha is not a free service, you should charge some money to use it. However, it is cheap enough if you just need to run for testing.  
https://anti-captcha.com/zh

### 3. Prepare the correct chrome driver depend on your environment

You can follow this site to see your chrome version.  
https://support.google.com/chrome/a/answer/10025748?hl=en

Make sure to download the correct version and put the chromedriver.exe to the driver folder in this project.  
https://chromedriver.chromium.org/downloads

## Let's get started
This program needs some personal data to buy the tickets. You can just replace the parameters in example.cmd in the project folder run it.

The following is the content of example.cmd.

```
python BuyTicket.py ^
--id {your_id} ^
--trip 1 ^
--email {your_email_address} ^
--key {your_api_key} ^
--startingstation 南港 ^
--destination 台南 ^
--start 2023/09/28 ^
--end 2023/10/01 ^
--totrainnumber 249 ^
--backtrainnumber 1238 ^
--date 2023/09/3 ^
--timer 02:00:00
```
And you can refer to the following statments to enter your data.
```
options:
  -h, --help            show this help message and exit
  --id ID               Please enter your id.(required)
  --ismember ISMEMBER   Are you the member of THSR? (yes/no)
  --phone PHONE         Please enter your phone.
  --email EMAIL         Please enter your email.
  --key KEY             Please enter the api key that you get from anticaptcha.(required)
  --trip TRIP           1 for one-way and 2 for round-trip ticket.
  --startingstation STARTINGSTATION
                        Please enter the starting station.(required)
  --destination DESTINATION
                        Please enter the destination.(required)
  --start START         Please enter the date you want to go. (YYYY/MM/DD)(required)
  --end END             Please enter the date you want to back. (YYYY/MM/DD)
  --totrainnumber TOTRAINNUMBER
                        Please enter the train number that you will take to go.(required)
  --backtrainnumber BACKTRAINNUMBER
                        Please enter the train number that you will take to back.
  --tickets TICKETS     How many tickets that you want to buy.
  --date DATE           When would you want to start the program? (YYYY/MM/DD)
  --timer TIMER         When would you want to start the program? (HH:MM:SS)
```
Then you can enjoy buying tickets automatically! 

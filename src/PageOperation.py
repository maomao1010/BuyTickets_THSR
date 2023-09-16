from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from src.Anticaptcha import *
import uuid

def HomePage(browser, TravelDatas, APIKey):
    captcha = "ABCD"
    count = 0
    
    #If the captcha is wrong, we have 5 change to retry.
    while count < 5:
        
        try:
            SearchByTrainNumber = browser.find_element(By.XPATH,'//*[@id="BookingS1Form"]/div[2]/div[2]/div/label[2]/input')
            StartStation = Select(browser.find_element(By.NAME,'selectStartStation'))
            DestinationStation = Select(browser.find_element(By.NAME,'selectDestinationStation'))
            toTrainNumber = browser.find_element(By.NAME,'toTrainIDInputField')
            TicketAmount = Select(browser.find_element(By.NAME,'ticketPanel:rows:0:ticketAmount'))
            Img = browser.find_element(By.ID,'BookingS1Form_homeCaptcha_passCode')
            CaptchaBox = browser.find_element(By.NAME,"homeCaptcha:securityCode")
            SubmitButton = browser.find_element(By.ID,"SubmitButton")      
            ChangeStartScript = "document.getElementById('toTimeInputField').value = arguments[0]"
            ChangeEndScript = "document.getElementById('backTimeInputField').value = arguments[0]"
        except:
            count += 1
            continue
                    
        SearchByTrainNumber.click()
        StartStation.select_by_visible_text(TravelDatas["From"])
        DestinationStation.select_by_visible_text(TravelDatas["To"])
        toTrainNumber.clear()
        toTrainNumber.send_keys(TravelDatas["toTrainNumber"])
        TicketAmount.select_by_visible_text(TravelDatas["Tickets"])
        browser.execute_script(ChangeStartScript, TravelDatas["Start"])
        id = str(uuid.uuid4())
        get_captcha(browser,Img,'result/captcha-' + id + '.png')
        captcha = parse_captcha('result/captcha-' + id + '.png', APIKey)
        CaptchaBox.send_keys(captcha)
                    
        if TravelDatas["Trip"] == "2":
            Trip = Select(browser.find_element(By.ID,'BookingS1Form_tripCon_typesoftrip'))
            backTrainNumber = browser.find_element(By.NAME,'backTrainIDInputField')
                
            Trip.select_by_visible_text("去回程")
            browser.execute_script(ChangeEndScript, TravelDatas["End"])
            backTrainNumber.clear()
            backTrainNumber.send_keys(TravelDatas["backTrainNumber"])
            
        SubmitButton.click()
        
        try:
            browser.find_element(By.ID,"idNumber")
            break
        except:
            count += 1

    
def ConfirmPage(browser, UserDatas):
    
    if UserDatas["IsMember"]:
        Member =  browser.find_element(By.ID,"memberSystemRadio1")
        MembershipCheckBox = browser.find_element(By.ID,"memberShipCheckBox")
        
        Member.click()
        MembershipCheckBox.click()

    IdNumber = browser.find_element(By.ID,"idNumber")
    Phone = browser.find_element(By.ID,"mobilePhone")
    Email = browser.find_element(By.ID,"email")
    AgreeBox = browser.find_element(By.XPATH,"//*[@id='BookingS3FormSP']/section[2]/div[3]/div[1]/label/input")
    SubmitButton = browser.find_element(By.ID,"isSubmit")     
    
    IdNumber.send_keys(UserDatas["ID"])
    Phone.send_keys(UserDatas["Phone"])
    Email.send_keys(UserDatas["Email"])
    AgreeBox.click()
    SubmitButton.click()    
    
    if UserDatas["IsMember"]:
        ConfirmButton = browser.find_element(By.ID, "btn-custom2")
        ConfirmButton.click()
    id = str(uuid.uuid4())

    browser.save_screenshot("result/ReserveData" + id + ".png")
    browser.close()
        
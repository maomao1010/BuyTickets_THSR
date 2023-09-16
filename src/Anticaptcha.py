from PIL import Image
from anticaptchaofficial.imagecaptcha import *
from io import BytesIO

import requests
import base64
import time

def get_captcha(browser, element, path):
    browser.save_screenshot(path)          
    location = element.location           
    size = element.size                   
    left = location['x']                  
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    image = Image.open(path)              
    image = image.crop((left, top, right, bottom)) 
    image.save(path, 'png')
    time.sleep(0.5)

def parse_captcha(image_path,apikey):
    buffer = BytesIO()
    image = Image.open(image_path)
    image.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    data = {
        "clientKey":apikey,
        "task": {
            "type": "ImageToTextTask",
            "body": img_str,
            "phrase":False,
            "case": True,
            "numeric": 0,
            "math": 0,
            "minLength": 4,
            "maxLength": 4
        }
    }
    r = requests.post("https://api.anti-captcha.com/createTask", json=data)
    r.raise_for_status()
    task_id = r.json()['taskId']
    ret = ""
    while True:
        data = {
            "clientKey":apikey,
            'taskId': task_id
        }
        r = requests.post("https://api.anti-captcha.com/getTaskResult", json=data)
        r.raise_for_status()
        if r.json()['status'] == 'ready':
            ret = r.json()['solution']['text']
            break
        time.sleep(1)
        
    return ret    
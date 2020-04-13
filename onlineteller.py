import time
from selenium import webdriver as w
import smtplib
driver= w.Chrome()
driver.get('https:web.whatsapp.com')
time.sleep(30)
name=input('enter the target person name ')
user = driver.find_element_by_xpath('//span[@title= "{}"]'.format(name))
user.click()
while True:
    state= driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header')
    s=state.text
    if 'online' in s:
        print('target is in online')
        break

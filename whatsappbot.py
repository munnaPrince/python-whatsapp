import time
from selenium import webdriver as w
import smtplib
driver= w.Chrome()
driver.get('https:web.whatsapp.com')
time.sleep(30)
while True:
    state= driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header')
    s=state.text
    print(s)
    if 'online' in s:
        email='munnaf.prince.48@gmail.com'
        password='Loveudad2@'
        send_to_email='munnaf.prince.48@gmail.com'
        msg='targeted person is in online '
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,send_to_email,msg)
        server.quit()
        time.sleep(100)
        


    

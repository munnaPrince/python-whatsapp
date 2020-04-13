from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('enter the group name ')
msg=input('enter the msg')
count=int(input('enter the count of message'))
input('enter after scanning')
user = driver.find_element_by_xpath('//span[@title= "{}"]'.format(name))
user.click()
msg_box =driver.find_element_by_class_name('_1Plpp')
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()

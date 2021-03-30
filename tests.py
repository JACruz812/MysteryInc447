import time
from selenium import webdriver

#This example requires Selenium WebDriver 3.13 or newer
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe')
driver.get('http://127.0.0.1:8000/accounts/login/')
time.sleep(2)  # Wait 2 secs

#test logging in with a fake user
driver.get('http://127.0.0.1:8000/accounts/login/')
id_input = driver.find_element_by_id('id_username') #set id_input var
pass_input = driver.find_element_by_id('id_password') #set pass_input var
id_input.clear()
pass_input.clear()
id_input.send_keys('johnDoe1')
pass_input.send_keys('flowerCats')
time.sleep(2)  # Wait 2 secs
driver.find_element_by_id('loginButton').click() #click sign up
time.sleep(2)  # Wait 2 secs

#enter signup page
driver.find_element_by_id('signupButton').click() #test signup button



#attempt inputing an invalid username
id_input = driver.find_element_by_id('id_username') #set id_input var
pass1_input = driver.find_element_by_id('id_password1') #set pass1_input var
pass2_input = driver.find_element_by_id('id_password2') #set pass2_input var
id_input.send_keys('|hi|')
pass1_input.send_keys('Flowers1234')
pass2_input.send_keys('Flowers1234')
driver.find_element_by_id('submitButton').click() #click sign up
time.sleep(2)  # Wait 2 secs

#attempt inputing a common password
id_input = driver.find_element_by_id('id_username') #set id_input var
pass1_input = driver.find_element_by_id('id_password1') #set pass1_input var
pass2_input = driver.find_element_by_id('id_password2') #set pass2_input var
id_input.clear()
id_input.send_keys('johnDoe1')
pass1_input.send_keys('Password123')
pass2_input.send_keys('Password123')
driver.find_element_by_id('submitButton').click() #click sign up
time.sleep(2)  # Wait 2 secs

#attempt inputing an invalid password
id_input = driver.find_element_by_id('id_username') #set id_input var
pass1_input = driver.find_element_by_id('id_password1') #set pass1_input var
pass2_input = driver.find_element_by_id('id_password2') #set pass2_input var
id_input.clear()
id_input.send_keys('johnDoe1')
pass1_input.send_keys('123456789')
pass2_input.send_keys('123456789')
driver.find_element_by_id('submitButton').click() #click sign up
time.sleep(2)  # Wait 2 secs

#attempt inputing an invalid password
id_input = driver.find_element_by_id('id_username') #set id_input var
pass1_input = driver.find_element_by_id('id_password1') #set pass1_input var
pass2_input = driver.find_element_by_id('id_password2') #set pass2_input var
id_input.clear()
id_input.send_keys('johnDoe1')
pass1_input.send_keys('flowerCats')
pass2_input.send_keys('flowerCats')
driver.find_element_by_id('submitButton').click() #click sign up
time.sleep(2)  # Wait 2 secs

#test continue and return buttons
driver.find_element_by_id('continueButton').click() #continue to create page
time.sleep(2) #wait 2 secs
driver.find_element_by_id('returnHomeButton').click() #continue to create page
time.sleep(2)

#test using the new login
driver.get('http://127.0.0.1:8000/accounts/login/')
id_input = driver.find_element_by_id('id_username') #set id_input var
pass_input = driver.find_element_by_id('id_password') #set pass_input var
id_input.clear()
pass_input.clear()
id_input.send_keys('johnDoe1')
pass_input.send_keys('flowerCats')
time.sleep(2)  # Wait 2 secs
driver.find_element_by_id('loginButton').click() #click sign up


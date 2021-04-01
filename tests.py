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
id_input.send_keys('p')
pass_input.send_keys('a')
time.sleep(2)  # Wait 2 secs
driver.find_element_by_id('loginButton').click() #click sign up
time.sleep(2)  # Wait 2 secs

#enter signup page
driver.find_element_by_id('signupButton').click() #test signup button

#attempt signing up a user
id_input = driver.find_element_by_id('id_username') #set id_input var
pass1_input = driver.find_element_by_id('id_password1') #set pass1_input var
pass2_input = driver.find_element_by_id('id_password2') #set pass2_input var
id_input.clear()
id_input.send_keys('randUser2')
pass1_input.send_keys('flowerCats')
pass2_input.send_keys('flowerCats')
driver.find_element_by_id('submitButton').click() #click sign up
time.sleep(2)  # Wait 2 secs

#user may already exist so login at the login page
driver.get('http://127.0.0.1:8000/accounts/login/')
id_input = driver.find_element_by_id('id_username') #set id_input var
pass_input = driver.find_element_by_id('id_password') #set pass_input var
id_input.clear()
pass_input.clear()
id_input.send_keys('randUser2')
pass_input.send_keys('flowerCats')
time.sleep(2)  # Wait 2 secs
driver.find_element_by_id('loginButton').click() #click sign up
time.sleep(2)  # Wait 2 secs

#test continue and return buttons
driver.find_element_by_id('continueButton').click() #continue to create page
time.sleep(2) #wait 2 secs
driver.find_element_by_id('returnHomeButton').click() #continue to create page
time.sleep(2)

#test logout button
driver.find_element_by_id('logoutButton').click()#from the storyboard page logout the user and return to the login page
time.sleep(2)

#test logging an existing user back in
id_input = driver.find_element_by_id('id_username') #set id_input var
pass_input = driver.find_element_by_id('id_password') #set pass_input var
id_input.clear()
pass_input.clear()
id_input.send_keys('randUser2')
pass_input.send_keys('flowerCats')
time.sleep(2)  # Wait 2 secs
driver.find_element_by_id('loginButton').click() #click sign up

#test logout button
time.sleep(2)
driver.find_element_by_id('logoutButton').click()#from the home page logout the user and return to the login page

#return to the home page to ensure the user is logged out(page should display "You are not logged in")
time.sleep(2)
driver.get('http://127.0.0.1:8000')
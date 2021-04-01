import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass

    def test_site(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        id_input = self.selenium.find_element_by_id('id_username')  # set id_input var
        pass_input = self.selenium.find_element_by_id('id_password') #set pass_input var
        id_input.clear()
        pass_input.clear()
        id_input.send_keys('johnDoe1')
        pass_input.send_keys('flowerCats')
        time.sleep(2)  # Wait 2 secs
        self.selenium.find_element_by_id('loginButton').click() #click sign up
        time.sleep(2)  # Wait 2 secs

        #enter signup page
        self.selenium.find_element_by_id('signupButton').click() #test signup button
        time.sleep(2)  # Wait 2 secs

        #attempt inputing an invalid username
        id_input = self.selenium.find_element_by_id('id_username') #set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1') #set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2') #set pass2_input var
        id_input.send_keys('|hi|')
        pass1_input.send_keys('Flowers1234')
        pass2_input.send_keys('Flowers1234')
        self.selenium.find_element_by_id('submitButton').click() #click sign up
        time.sleep(2)  # Wait 2 secs
        
        #attempt inputing a common password
        id_input = self.selenium.find_element_by_id('id_username') #set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1') #set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2') #set pass2_input var
        id_input.clear()
        id_input.send_keys('johnDoe1')
        pass1_input.send_keys('Password123')
        pass2_input.send_keys('Password123')
        self.selenium.find_element_by_id('submitButton').click() #click sign up
        time.sleep(2)  # Wait 2 secs
        
        #attempt inputing an invalid password
        id_input = self.selenium.find_element_by_id('id_username') #set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1') #set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2') #set pass2_input var
        id_input.clear()
        id_input.send_keys('johnDoe1')
        pass1_input.send_keys('123456789')
        pass2_input.send_keys('123456789')
        self.selenium.find_element_by_id('submitButton').click() #click sign up
        time.sleep(2)  # Wait 2 secs
        
        #attempt inputing an invalid password
        id_input = self.selenium.find_element_by_id('id_username') #set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1') #set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2') #set pass2_input var
        id_input.clear()
        id_input.send_keys('johnDoe1')
        pass1_input.send_keys('flowerCats')
        pass2_input.send_keys('flowerCats')
        self.selenium.find_element_by_id('submitButton').click() #click sign up
        time.sleep(2)  # Wait 2 secs
        
        #test continue and return buttons
        self.selenium.find_element_by_id('continueButton').click() #continue to create page
        time.sleep(2) #wait 2 secs
        self.selenium.find_element_by_id('returnHomeButton').click() #continue to create page
        time.sleep(2)
        
        #test using the new login
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        id_input = self.selenium.find_element_by_id('id_username') #set id_input var
        pass_input = self.selenium.find_element_by_id('id_password') #set pass_input var
        id_input.clear()
        pass_input.clear()
        id_input.send_keys('johnDoe1')
        pass_input.send_keys('flowerCats')
        time.sleep(2)  # Wait 2 secs
        self.selenium.find_element_by_id('loginButton').click() #click sign up
        time.sleep(2)








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
        self.selenium.switch_to.alert.accept()
        time.sleep(1)
        self.selenium.find_element_by_id('logoutButton').click() #logout from home page
        id_input = self.selenium.find_element_by_id('id_username') #set id_input var
        pass_input = self.selenium.find_element_by_id('id_password') #set pass_input var
        id_input.clear()
        pass_input.clear()
        id_input.send_keys('johnDoe1')
        pass_input.send_keys('flowerCats')
        time.sleep(2)  # Wait 2 secs
        self.selenium.find_element_by_id('loginButton').click() #click sign up
        time.sleep(1)
        self.selenium.find_element_by_id('continueButton').click() #click sign up

        # Sets the title and synopsis values to a default allowing for visual on
        # if they are saved on refresh
        self.selenium.find_element_by_id('title').send_keys('new story')
        time.sleep(1)
        self.selenium.find_element_by_id('synopsis').send_keys('This is a new story testing adding and removing clues.')
        time.sleep(1)

        # Adds a new clue that only contains text leaving the image blank
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)
        self.selenium.find_element_by_id('clue1_text').send_keys('This is clue 1')
        time.sleep(1)

        # Adds a new clue that contains both text and an image
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)
        self.selenium.find_element_by_id('clue2_text').send_keys('This is clue 2')
        time.sleep(1)
        self.selenium.find_element_by_id('clue2_img_url').send_keys('https://media.tenor.com/images/1ef18fe44fec6a28182fe0b60d2e9e94/tenor.gif')
        time.sleep(1)

        # Refreshes the content on the webpage so the image will be presented
        self.selenium.find_element_by_id('refresh').click()
        time.sleep(1)

        # Adds another clue that only contains text
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)
        self.selenium.find_element_by_id('clue3_text').send_keys('This is clue 3')
        time.sleep(1)

        # Marks the first and third clues for removal
        self.selenium.find_element_by_id('clue1_remove').click()
        time.sleep(1)
        self.selenium.find_element_by_id('clue3_remove').click()
        time.sleep(1)

        # Fully removes all marked clues from the story
        self.selenium.find_element_by_id('remove').click()
        time.sleep(1)

        # Focus on the alert and accept
        self.selenium.switch_to.alert.accept()
        time.sleep(1)

        # Click the new story button and accept
        self.selenium.find_element_by_id('new_story').click()
        time.sleep(1)

        # Focus on the alert and accept
        self.selenium.switch_to.alert.accept()
        time.sleep(1)






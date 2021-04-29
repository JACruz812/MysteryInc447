import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver

# This function is used to check if an element exists
# if an exception is thrown when trying to find it then it must not exist
def existsElement(self, el_id):
    try:
        self.selenium.find_element(el_id)
    except:
        return False
    return True



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
        pass_input = self.selenium.find_element_by_id('id_password')  # set pass_input var
        id_input.clear()
        pass_input.clear()
        id_input.send_keys('johnDoe1')
        pass_input.send_keys('flowerCats')
        time.sleep(1)  # Wait 2 secs
        self.selenium.find_element_by_id('loginButton').click()  # click sign up
        time.sleep(1)  # Wait 2 secs

        # enter signup page
        self.selenium.find_element_by_id('signupButton').click()  # test signup button
        time.sleep(1)  # Wait 2 secs

        #log in
        id_input = self.selenium.find_element_by_id('id_username')  # set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1')  # set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2')  # set pass2_input var
        id_input.clear()
        id_input.send_keys('johnDoe1')
        pass1_input.send_keys('flowerCats')
        pass2_input.send_keys('flowerCats')
        self.selenium.find_element_by_id('submitButton').click()  # click sign up
        time.sleep(1)  # Wait 2 secs

        # test continue and return buttons
        self.selenium.find_element_by_id('continueButton').click()  # continue to create page
        time.sleep(1)  # wait 1 secs
        self.selenium.find_element_by_id('returnHomeButton').click()  # return to home page
        time.sleep(1)

        # test using the new login
        self.selenium.switch_to.alert.accept()
        time.sleep(1)
        self.selenium.find_element_by_id('logoutButton').click()  # logout from home page
        id_input = self.selenium.find_element_by_id('id_username')  # set id_input var
        pass_input = self.selenium.find_element_by_id('id_password')  # set pass_input var
        id_input.clear()
        pass_input.clear()
        id_input.send_keys('johnDoe1')
        pass_input.send_keys('flowerCats')
        time.sleep(1)  # Wait 1 sec
        self.selenium.find_element_by_id('loginButton').click()  # click log in
        time.sleep(1)
        self.selenium.find_element_by_id('continueButton').click()  # click enter storyboard creator

        # add clues, log out and ensure the data has saved
        self.selenium.find_element_by_id('add').click()
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)
        self.selenium.find_element_by_id('clue1_text').send_keys('Important Information 1')
        time.sleep(1)
        self.selenium.find_element_by_id('clue2_text').send_keys('Important Information 2')
        time.sleep(1)
        self.selenium.find_element_by_id('save').click()
        self.selenium.find_element_by_id('returnHomeButton').click()  # return to home page
        self.selenium.switch_to.alert.accept()
        time.sleep(1)  # Wait 1 sec
        self.selenium.find_element_by_id('logoutButton').click()  # logout
        id_input = self.selenium.find_element_by_id('id_username')  # set id_input var
        pass_input = self.selenium.find_element_by_id('id_password')  # set pass_input var
        id_input.clear()
        pass_input.clear()
        id_input.send_keys('johnDoe1')
        pass_input.send_keys('flowerCats')
        time.sleep(1)  # Wait 1 sec
        self.selenium.find_element_by_id('loginButton').click()  # login
        time.sleep(1)
        self.selenium.find_element_by_id('continueButton').click()  # click enter storyboard creator
        # use assert to check that the value of clue1 and clue2 are still present
        self.assertEqual(self.selenium.find_element_by_id('clue1_text').get_attribute("value"), "Important "
                                                                                                "Information 1")
        self.assertEqual(self.selenium.find_element_by_id('clue2_text').get_attribute("value"), "Important "
                                                                                                "Information 2")
        time.sleep(1)

        # start a new story and check that the previous values don't exist anymore
        self.selenium.find_element_by_id('returnHomeButton').click()  # return to home page
        self.selenium.switch_to.alert.accept()
        time.sleep(1)  # Wait 1 sec
        self.selenium.find_element_by_id('submitButton').click()  # click enter storyboard creator
        self.assertFalse(existsElement(self, 'clue1_text'))


        # Test that the print button works and displays properly
        self.selenium.find_element_by_id('title').send_keys('This is the Title')
        time.sleep(1)
        self.selenium.find_element_by_id('synopsis').send_keys('This story is going to be about how developers develop'
                                                               'And without developing they would likely all fall into'
                                                               'an abyss of internet weirdness')
        time.sleep(1)
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)
        self.selenium.find_element_by_id('clue1_text').send_keys('This is clue 1, there will not be any pictures here')
        time.sleep(1)
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)
        self.selenium.find_element_by_id('clue2_text').send_keys('This is clue 2, a meme is attached to this one')
        time.sleep(1)
        self.selenium.find_element_by_id('clue2_img_url').send_keys(
            'https://i.pinimg.com/originals/d9/1b/ca/d91bca90801304269c6091071cd051e6.jpg')
        time.sleep(1)
        self.selenium.find_element_by_id('save').click()
        self.selenium.find_element_by_id('print').click()
        time.sleep(2)
        self.selenium.back()
        time.sleep(1)






import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from django.test import TestCase
from conf.models import Story, Clue


# Holds the tests for the database tables
class database_tests(TestCase):

    # tests to see the functionality of saving and removing a story to and from the database
    def Story_test(self):
        s = Story(title="testing", synopsis='This is a test', num_clues=0, user='admin')
        s.save()
        self.assertTrue(len(Story.objects.filter(title='testing', user='admin')) == 0, msg='story correctly saved')
        s.delete()
        self.assertTrue(len(Story.objects.filter(title='testing', user='admin')) == 0, msg='story correctly removed')

    # tests to see the functionality of saving clues within the database while having them connected to a story
    def Clue_test(self):
        s = Story(title="testing", synopsis='This is a test', num_clues=0, user='admin')
        s.save()
        self.assertTrue(len(s.clue_set.all()) == 0, msg='no clues connected to new story')
        s.clue_set.create(clue_id=1, clue_num=1, clue_text='testing1', clue_img_url='', parent_list='[]')
        s.clue_set.create(clue_id=2, clue_num=2, clue_text='testing2', clue_img_url='', parent_list='[]')
        self.assertTrue(len(s.clue_set.all()) == 2, msg='clues have been saved to story')
        c = s.clue_set.get(clue_id=1)
        c.delete()
        self.assertTrue(len(s.clue_set.all()) == 1, msg='single clue has been removed from story')
        s.clue_set.all().delete()
        self.assertTrue(len(s.clue_set.all()) == 0, msg='clues have been removed from story')
        s.delete()


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
        time.sleep(2)  # Wait 2 secs
        self.selenium.find_element_by_id('loginButton').click()  # click sign up
        time.sleep(2)  # Wait 2 secs

        # enter signup page
        self.selenium.find_element_by_id('signupButton').click()  # test signup button
        time.sleep(2)  # Wait 2 secs

        # attempt inputing an invalid username
        id_input = self.selenium.find_element_by_id('id_username')  # set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1')  # set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2')  # set pass2_input var
        id_input.send_keys('|hi|')
        pass1_input.send_keys('Flowers1234')
        pass2_input.send_keys('Flowers1234')
        self.selenium.find_element_by_id('submitButton').click()  # click sign up
        time.sleep(2)  # Wait 2 secs

        # attempt inputing a common password
        id_input = self.selenium.find_element_by_id('id_username')  # set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1')  # set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2')  # set pass2_input var
        id_input.clear()
        id_input.send_keys('johnDoe1')
        pass1_input.send_keys('Password123')
        pass2_input.send_keys('Password123')
        self.selenium.find_element_by_id('submitButton').click()  # click sign up
        time.sleep(2)  # Wait 2 secs

        # attempt inputing an invalid password
        id_input = self.selenium.find_element_by_id('id_username')  # set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1')  # set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2')  # set pass2_input var
        id_input.clear()
        id_input.send_keys('johnDoe1')
        pass1_input.send_keys('123456789')
        pass2_input.send_keys('123456789')
        self.selenium.find_element_by_id('submitButton').click()  # click sign up
        time.sleep(2)  # Wait 2 secs

        # attempt inputing an invalid password
        id_input = self.selenium.find_element_by_id('id_username')  # set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1')  # set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2')  # set pass2_input var
        id_input.clear()
        id_input.send_keys('johnDoe1')
        pass1_input.send_keys('flowerCats')
        pass2_input.send_keys('flowerCats')
        self.selenium.find_element_by_id('submitButton').click()  # click sign up

        # test continue and return buttons
        self.selenium.find_element_by_id('continueButton').click()  # continue to create page
        time.sleep(2)  # wait 2 secs
        self.selenium.find_element_by_id('returnHomeButton').click()  # continue to create page
        time.sleep(2)

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
        time.sleep(2)  # Wait 2 secs
        self.selenium.find_element_by_id('loginButton').click()  # click sign up
        time.sleep(2)

        # Sets the title and synopsis values to a default allowing for visual on
        # if they are saved on refresh
        self.selenium.find_element_by_id('title').send_keys('new story')
        time.sleep(1)
        self.selenium.find_element_by_id('synopsis').send_keys('This is a new story testing adding and removing clues.')
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
        self.selenium.find_element_by_id('clue2_img_url').send_keys(
            'https://media.tenor.com/images/1ef18fe44fec6a28182fe0b60d2e9e94/tenor.gif')
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
        # Marks the first and third clues for removal
        self.selenium.find_element_by_id('clue1_remove').click()
        
        time.sleep(1)
        self.selenium.find_element_by_id('clue1_text').send_keys('This is clue 1, there will not be any pictures here')
        time.sleep(1)
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)
        # checks parent clues
        clue2 = Clue.objects.get().first()
        assertEquals(clue2.num_parents, 0)

        # Focus on the alert and accept
        self.selenium.switch_to.alert.accept()
        time.sleep(1)
        self.selenium.find_element_by_id('clue2_img_url').send_keys(
            'https://i.pinimg.com/originals/d9/1b/ca/d91bca90801304269c6091071cd051e6.jpg')
        time.sleep(1)
        self.selenium.find_element_by_id('save').click()
        self.selenium.find_element_by_id('print').click()
        time.sleep(2)
        self.selenium.back()
        time.sleep(1)


    # tests that the button on the display clue page that allows for the user
    # to return to the storyboard editor still works
    def test_return_to_storyboard_button(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/display_clues/'))

        # Adds a new clue that only contains text leaving the image blank
        self.selenium.find_element_by_id('returnToEditor').click()
        time.sleep(1)

        assertEquals(driver.getCurrentUrl(), (self.live_server_url, '/return_to_editor/'))



    # checks if the display clue page contatins the correct information
    # without first refreshing the storyboard page to save clue information
    def test_display_clue_page_no_refresh(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/return_to_editor/'))

        # Adds a new clue that only contains text leaving the image blank
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)
        self.selenium.find_element_by_id('clue1_text').send_keys('This is clue 1')
        time.sleep(1)

        # Adds a new clue that only contains text leaving the image blank
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)

        # Adds a new clue that only contains text leaving the image blank
        self.selenium.find_element_by_id('displayclues').click()
        time.sleep(1)

        assertEquals(driver.getCurrentUrl(), (self.live_server_url, '/display_clues/'))


    # checks that the visual display clues page looks correct after a storyboard refresh and 
    # retains all of the clue information, escpeially the clue text
    def test_display_clues_with_refresh(self):

        # go back to storyboard editor
        self.selenium.get('%s%s' % (self.live_server_url, '/return_to_editor/'))

        # Adds a new clue that only contains text leaving the image blank
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)
        self.selenium.find_element_by_id('clue1_text').send_keys('This is clue 1')
        time.sleep(1)

        # Adds a new clue that only contains text leaving the image blank
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)

        # Adds a new clue that only contains text leaving the image blank
        self.selenium.find_element_by_id('refresh').click()
        time.sleep(1)

        # Adds a new clue that only contains text leaving the image blank
        self.selenium.find_element_by_id('displayclues').click()
        time.sleep(1)

        assertEquals(driver.getCurrentUrl(), (self.live_server_url, '/display_clues/'))



        






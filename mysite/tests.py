import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from django.test import TestCase
from conf.models import Story, Clue


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

        # enter signup page
        self.selenium.find_element_by_id('signupButton').click()  # test signup button
        time.sleep(1)  # Wait 2 secs

        # create a user
        id_input = self.selenium.find_element_by_id('id_username')  # set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1')  # set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2')  # set pass2_input var
        id_input.clear()
        id_input.send_keys('johnDoe1')
        pass1_input.send_keys('flowerCats')
        pass2_input.send_keys('flowerCats')
        self.selenium.find_element_by_id('submitButton').click()  # click sign up

        # start a new story
        self.selenium.find_element_by_id('continueButton').click()  # continue to create page
        time.sleep(1)  # wait 2 secs

        # Sets the title and synopsis values to a default allowing for visual on
        # if they are saved on refresh
        self.selenium.find_element_by_id('title').send_keys('Title of Story')
        time.sleep(1)
        self.selenium.find_element_by_id('synopsis').send_keys('Dave found joy in the daily routine of life. He awoke '
                                                               'at the same time, ate the same breakfast and drove the '
                                                               'same commute. He worked at a job that never seemed to '
                                                               'change and he got home at 6 pm sharp every night. It '
                                                               'was who he had been for the last ten years and he had '
                                                               'no idea that was all about to change. The leather '
                                                               'jacked showed the scars of being his ')
        time.sleep(1)

        # add clues and clue data then save
        self.selenium.find_element_by_id('add').click()
        self.selenium.find_element_by_id('add').click()
        self.selenium.find_element_by_id('add').click()
        time.sleep(1)
        self.selenium.find_element_by_id('clue1_text').send_keys('favorite for years. it wore those scars with pride, '
                                                                 'feeling that they enhanced his presence rather than'
                                                                 ' diminishing it. The scars gave it character and had '
                                                                 'not overwhelmed to the point that it had become '
                                                                 'ratty. The jacket was in its prime and it knew it.')
        self.selenium.find_element_by_id('clue1_img_url').send_keys('https://i.ytimg.com/vi/Yj7ja6BANLM/maxresdefault.jpg')
        time.sleep(1)
        self.selenium.find_element_by_id('clue2_text').send_keys('Sitting in the sun, away from everyone who had done '
                                                                 'him harm in the past, he quietly listened to those '
                                                                 'who roamed by. He felt at peace in the moment, hoping'
                                                                 ' it would last, but knowing the reprieve would soon '
                                                                 'come to an end. He closed his eyes, the sun beating '
                                                                 'down on face and he smiled. He smiled for the first '
                                                                 'time in as long as he could remember.')
        self.selenium.find_element_by_id('clue2_clue_parents').send_keys('1')
        self.selenium.find_element_by_id('clue2_img_url').send_keys('https://cdn.shopify.com/s/files/1/0160/2840/1712/products/crab-sand-min.png?v=1618357432')
        time.sleep(1)
        self.selenium.find_element_by_id('clue3_text').send_keys('Balloons are pretty and come in different colors, '
                                                                 'different shapes, different sizes, and they can even '
                                                                 'adjust sizes as needed. But do not make them too big '
                                                                 'or they might just pop, and then bye-bye balloon. It'
                                                                 ' will  be gone and lost for the rest of mankind. They'
                                                                 ' can serve a variety of purposes, from decorating to'
                                                                 ' water balloon wars. You just have to use your head '
                                                                 'to think a little bit about what to do with them.')
        self.selenium.find_element_by_id('clue3_clue_parents').send_keys('1,2')
        self.selenium.find_element_by_id('clue3_img_url').send_keys('https://cdn.cnn.com/cnnnext/dam/assets/170704145417-urkel-1-full-169.jpg')
        self.selenium.find_element_by_id('save').click()

        # enter print page and assert check the child values
        self.selenium.find_element_by_id('print').click()
        time.sleep(5)
        self.assertEqual(self.selenium.find_element_by_id('clue1_clue_children').text, 'Clue 2, Clue 3,')
        self.assertEqual(self.selenium.find_element_by_id('clue2_clue_children').text, 'Clue 3,')
        self.assertEqual(self.selenium.find_element_by_id('clue3_clue_children').text, '')
        self.selenium.back()
        time.sleep(1)

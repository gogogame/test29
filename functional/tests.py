from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

# Create your tests here.

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_question_and_retrieve_it_later(self):
        # I need to make a quiz app, so it begin
        self.browser.get(self.live_server_url)

        # Title is correct
        self.assertIn('Quiz', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Quiz', header_text)

        #
        #inputbox = self.browser.find_element_by_id('Question')

        self.fail('Finish the test!')

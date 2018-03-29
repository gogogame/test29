from django.test import TestCase
from selenium import webdriver
from django.test import LiveServerTestCase

# Create your tests here.

# This is Functional tests

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

        # Still havn't done
        self.fail('Finish the test!')

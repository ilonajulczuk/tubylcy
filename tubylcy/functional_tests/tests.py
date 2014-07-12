from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_a_page_and_learn_more(self):
        # Jan heard about 'tubylcy' and want to check out its homepage
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention helping local community
        self.assertIn('Help your community', self.browser.title)
        # He wants to learn more about it
        more_button = self.browser.find_element_by_id('id_learn_more')
        more_button.click()

from django.test import LiveServerTestCase
from selenium import webdriver

class FunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(FunctionalTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(FunctionalTest, self).tearDown()

    def test_create_user(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/workflow/login/")
        )
from django.test import LiveServerTestCase
from pyvirtualdisplay import Display
from selenium import webdriver

class FunctionalTest(LiveServerTestCase):
    fixtures = ["initial_data.json"]
    
    def setUp(self):
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(FunctionalTest, self).setUp()

    def login(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/workflow/login/")
        )
        username = self.selenium.find_element_by_id("id_username")
        password = self.selenium.find_element_by_id("id_password")
        username.send_keys("zxiong")
        password.send_keys("tsl")
        login_submit = self.selenium.find_element_by_id("login")
        login_submit.click()

    def tearDown(self):
        self.selenium.quit()
        super(FunctionalTest, self).tearDown()

    def test_functions(self):
        self.login()
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/workflow/logout/")
        )


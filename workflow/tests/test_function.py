from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class FunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/workflow/login/")
        )
        username = self.selenium.find_element_by_id("id_username")
        password = self.selenium.find_element_by_id("id_password")
        username.send_keys("zxiong")
        password.send_keys("tsl")
        login_submit = self.selenium.find_element_by_id("login")
        login_submit.click()
        super(FunctionalTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(FunctionalTest, self).tearDown()

    def test_create_assignment(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/workflow/assignments/new/")
        )
        title = self.selenium.find_element_by_id("id_title")
        content = self.selenium.find_element_by_id("id_content")
        section = self.selenium.find_element_by_id("id_section")
        type = self.selenium.find_element_by_id("id_type")
        receiver = self.selenium.find_element_by_id("id_receiver")
        due_date = self.selenium.find_element_by_id("id_due_date")
        title.send_keys('Take photo of Oldenborg')
        content.send_keys('Go into Oldenborg during lunch, and take a picture of their apples')
        Select(section).select_by_visible_text("news")
        Select(type).select_by_visible_text("Photo Assignment")
        Select(receiver).select_by_visible_text("kshikama")
        due_date.clear()
        due_date.send_keys("03/11/2011")
        submit = self.selenium.find_element_by_id("submit_assignment")
        submit.click()
        title = self.selenium.find_element_by_css_selector('a[href="/workflow/assignments/2/"]')
        assert "Take photo of Oldenborg" in title.text

    def create_article_and_upload_photos(self):
        pass
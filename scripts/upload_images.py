from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Workflow Login Page
from website import settings

selenium = webdriver.Chrome()
selenium.maximize_window()
selenium.get("http://localhost:8000/workflow/album/85/2906/")
username = selenium.find_element_by_id("id_username")
password = selenium.find_element_by_id("id_password")
username.send_keys("zxiong")
password.send_keys("tsl")
login_submit = selenium.find_element_by_id("login")
login_submit.click()

# Workflow Album View Page
edit = selenium.find_element_by_id("edit")
edit.click()

# Workflow Album Edit Page
upload1 = selenium.find_element_by_id("id_photo_set-0-image")
upload1.send_keys(str(settings.BASE_DIR) + "/website/fixtures/goldengatebridge.jpg")
upload2 = selenium.find_element_by_id("id_photo_set-1-image")
upload2.send_keys(str(settings.BASE_DIR) + "/website/fixtures/pearlharbor.jpg")
upload3 = selenium.find_element_by_id("id_photo_set-1-image")
upload3.send_keys(str(settings.BASE_DIR) + "/website/fixtures/ramune.jpg")

submit = selenium.find_element_by_id("edit")
submit.click()

selenium.get("http://localhost:8000/workflow/logout/")
from selenium import webdriver

# Workflow Login Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from website import settings

selenium = webdriver.Chrome()
selenium.maximize_window()
selenium.get("http://localhost:8000/workflow/album/86/4263/")
username = selenium.find_element_by_id("id_username")
password = selenium.find_element_by_id("id_password")
username.send_keys("zxiong")
password.send_keys("tsl")
login_submit = selenium.find_element_by_id("login")
login_submit.click()

selenium.implicitly_wait(1)

# Workflow Album View Page
edit = selenium.find_element_by_id("edit")
edit.click()

# Workflow Album Edit Page
upload1 = selenium.find_element_by_id("id_photo_set-0-image")
upload1.send_keys(str(settings.BASE_DIR) + "/website/fixtures/goldengatebridge_thumbnail.jpg")
selenium.find_element_by_id("id_photo_set-0-credit-autocomplete").send_keys("kshikama")
author_select = WebDriverWait(selenium, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="id_photo_set-0-credit-wrapper"]/span[2]/span')))
author_select.click()

upload2 = selenium.find_element_by_id("id_photo_set-1-image")
upload2.send_keys(str(settings.BASE_DIR) + "/website/fixtures/pearlharbor_thumbnail.jpg")
selenium.find_element_by_id("id_photo_set-1-credit-autocomplete").send_keys("kshikama")
author_select = WebDriverWait(selenium, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="id_photo_set-1-credit-wrapper"]/span[2]/span')))
author_select.click()

submit = selenium.find_element_by_id("edit")
submit.click()

selenium.get("http://localhost:8000/workflow/logout/")
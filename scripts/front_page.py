from selenium import webdriver

# TODO: Fix

selenium = webdriver.Chrome()
selenium.maximize_window()
selenium.get("http://localhost:8000/workflow/front/")
username = selenium.find_element_by_id("id_username")
password = selenium.find_element_by_id("id_password")
username.send_keys("zxiong")
password.send_keys("tsl")
login_submit = selenium.find_element_by_id("login")
login_submit.click()

article1 = selenium.find_element_by_xpath('//*[@id="leftValues2"]/option[@value="4864"]')
article1.click()
btnRight = selenium.find_element_by_id('btnRight2')
btnRight.click()

submit = selenium.find_element_by_xpath('//*[@id="submit_button"]')
submit.click()

selenium.get("http://localhost:8000/workflow/logout/")
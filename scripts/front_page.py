from selenium import webdriver

# Workflow Login Page
from website import settings

selenium = webdriver.Chrome()
selenium.maximize_window()
selenium.get("http://localhost:8000/workflow/front/")
username = selenium.find_element_by_id("id_username")
password = selenium.find_element_by_id("id_password")
username.send_keys("zxiong")
password.send_keys("tsl")
login_submit = selenium.find_element_by_id("login")
login_submit.click()

article1 = selenium.find_element_by_xpath('//*[@id="leftValues2"]/option[@value="2906"]')
article1.click()
btnRight = selenium.find_element_by_id('btnRight2')
btnRight.click()
article2 = selenium.find_element_by_xpath('//*[@id="leftValues2"]/option[@value="2907"]')
article2.click()
btnRight.click()

article3 = selenium.find_element_by_xpath('//*[@id="leftValues"]/option[@value="2867"]')
article3.click()
btnRight2 = selenium.find_element_by_id('btnRight')
btnRight2.click()
article4 = selenium.find_element_by_xpath('//*[@id="leftValues"]/option[@value="2897"]')
article4.click()
article5 = selenium.find_element_by_xpath('//*[@id="leftValues"]/option[@value="2898"]')
article5.click()
article6 = selenium.find_element_by_xpath('//*[@id="leftValues"]/option[@value="2891"]')
article6.click()
article7 = selenium.find_element_by_xpath('//*[@id="leftValues"]/option[@value="2892"]')
article7.click()
article8 = selenium.find_element_by_xpath('//*[@id="leftValues"]/option[@value="2893"]')
article8.click()
article9 = selenium.find_element_by_xpath('//*[@id="leftValues"]/option[@value="2897"]')
article9.click()
btnRight2.click()

submit = selenium.find_element_by_xpath('//*[@id="submit_button"]')
submit.click()

selenium.get("http://localhost:8000/workflow/logout/")
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='../chromedriver')
driver.set_window_size(1108, 719)

driver.get("http://gsa-admin-dev.s3-website.eu-central-1.amazonaws.com/")

# ---LOGIN PAGE---
login_email_input = driver.find_element(By.XPATH, "//input[@type='email']")
login_email_input.send_keys("super_admin@gmail.com")

login_password_input = driver.find_element(By.XPATH, "//input[@type='password']")
login_password_input.send_keys('Qwerty123')

switch_admin_button = driver.find_element(By.XPATH, "//span[text()='Admin']").click()

login_button = driver.find_element(By.XPATH, "//button[@class='sc-kpOJdX sc-cMljjf cDWatm']").click()
time.sleep(3)

# ---CHOOSE REGION---
region_selector = driver.find_element(By.XPATH, "//div[@class='headerDropdown__indicator headerDropdown__dropdown-indicator css-tlfecz-indicatorContainer']").click()

choosen_region =driver.find_element(By.XPATH, "//div[text()='West Region']").click()

# ---COMPETITION FORM---
competitions_tab = driver.find_element(By.XPATH, "//a[@href='/competitions']").click()


breakpoint()
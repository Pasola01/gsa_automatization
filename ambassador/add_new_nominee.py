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
login_email_input.send_keys("jopio01@mailinator.com")

login_password_input = driver.find_element(By.XPATH, "//input[@type='password']")
login_password_input.send_keys('Password132')

switch_admin_button = driver.find_element(By.XPATH, "//span[text()='Admin']").click()

login_button = driver.find_element(By.XPATH, "//button[@class='sc-kpOJdX sc-cMljjf cDWatm']").click()
time.sleep(3)

# ---ADD NOMINEE FORM---
add_nominee_button = driver.find_element(By.XPATH, "//button[@class='sc-kpOJdX sc-dxgOiQ fSmGhC']").click()

nominee_name_input_field = driver.find_element(By.XPATH, "//input[@name='name']")
nominee_name_input_field.send_keys('user1')
time.sleep(3)

emil_input_field = driver.find_element(By.XPATH, "//input[@name='email']")
emil_input_field.send_keys('hello1@mailinator.com')

website_input_field = driver.find_element(By.XPATH, "//input[@name='webSite']")
website_input_field.send_keys('com.com')

competition_selector = driver.find_element(By.XPATH, "//div[@class='Dropdown-control']").click()

choosen_competition = driver.find_element(By.XPATH, "//div[text()='Automatisation Competition'][@class='Dropdown-option']").click()

category_selector = driver.find_element(By.XPATH, "//div[@class='rw-widget-input rw-widget-picker rw-widget-container']").click()
time.sleep(3)

category = driver.find_element(By.XPATH, "//span[text()='Best of... #1']").click()

nominees_country_selector = driver.find_element(By.XPATH, "//div[text()='Select an option']").click()

nominees_country = driver.find_element(By.XPATH, "//div[text()='Tanzania']").click()
time.sleep(3)

form = driver.find_element(By.XPATH, "//div[@class='ReactModal__Content ReactModal__Content--after-open']").send_keys(Keys.PAGE_DOWN)
time.sleep(3)

invite_button = driver.find_element(By.XPATH, "//button[@class='sc-kpOJdX sc-cMljjf cDWatm']").click()


breakpoint()





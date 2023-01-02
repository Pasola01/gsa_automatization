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
time.sleep(5)

add_compettition_button = driver.find_element(By.XPATH, "//button[text()='Add new competition']").click()

competition_name_input = driver.find_element(By.XPATH, "//input[@name='name']")
competition_name_input.send_keys("random competition 01")

competition_start_data = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[2]/div/div/div/div[1]/div/div/input").send_keys("12/01/22")
set_start_data = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[2]/div/div/div/div[1]/div/div/input").send_keys(Keys.ENTER)

competition_end_data = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[2]/div/div/div/div[2]/div/div/input").send_keys("12/28/22")
set_end_date =driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[2]/div/div/div/div[2]/div/div/input").send_keys(Keys.ENTER)
time.sleep(5)

category_selector = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[3]/div/div/div[1]").click()
time.sleep(5)

set_category = driver.find_element(By.XPATH, "//span[text()='Best Design']").click()

rioridan = driver.find_element(By.XPATH, "//input[@name='name']").click()

region_country_placeholder = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[5]/div/div/div").click()
time.sleep(7)
tansania_country = driver.find_element(By.XPATH, "//span[text()='Tanzania']").click()


breakpoint()

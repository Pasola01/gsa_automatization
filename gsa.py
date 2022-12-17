from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.set_window_size(1108, 719)

driver.get("http://gsa-admin-dev.s3-website.eu-central-1.amazonaws.com/")

login_email_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/form/div[1]/input')
login_email_input.send_keys("jopio01@mailinator.com")

login_password_input = driver.find_element(By.NAME, 'password')
login_password_input.send_keys('Password132')

switch_admin_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/ul/li[2]').click()

login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/form/button').click()
time.sleep(5)

add_nominee_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/button').click()

noninee_name_input = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/form/div[1]/div/label/input')
noninee_name_input.send_keys('user1')
time.sleep(5)

emil_input_field = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/form/div[2]/div/label/input')
emil_input_field.send_keys('hello1@mailinator.com')

website_input_field = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/form/div[3]/div/label/input')
website_input_field.send_keys('com.com')

competition_selector = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/form/div[4]/div/div/div/div').click()

select_competition = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/form/div[4]/div/div/div/div[2]').click()

category_selector = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/form/div[4]/div[2]/div/div/div').click()
time.sleep(3)

choosen_category = driver.find_element(By.ID, 'rw_1_listbox_active_option')
choosen_category.click()

nominees_country_selector = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/form/div[4]/div[3]/div/div/div').click()

selected_country = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/form/div[4]/div[3]/div/div/div[2]/div').click()
time.sleep(5)

invite_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/form/div[5]/button').click()


breakpoint()





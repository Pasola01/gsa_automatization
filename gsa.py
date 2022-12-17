from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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



breakpoint()


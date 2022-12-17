from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.set_window_size(1108, 719)
# driver.fullscreen_window()

driver.get('https://tc-rsfrontend-stage.herokuapp.com')
time.sleep(8)

skip_tutorial = driver.find_element(By.XPATH, '/html/body/div/div/div/div/a')
skip_tutorial.click()

close_massege = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/button')
close_massege.click()
time.sleep(5)

get_start_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/nav/a[5]')
get_start_button.click()

inpun_email_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/form/div[1]/div/input')
inpun_email_field.send_keys("benzema.tc@mailinator.com")

input_password_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/form/div[2]/div/input')
input_password_field.send_keys("Password%%%")

sign_in_button = driver.find_element(By.XPATH, '')
sign_in_button.click()


breakpoint()



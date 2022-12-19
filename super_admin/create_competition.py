from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='../chromedriver')
driver.set_window_size(1108, 719)

driver.get("http://gsa-admin-dev.s3-website.eu-central-1.amazonaws.com/")


breakpoint()
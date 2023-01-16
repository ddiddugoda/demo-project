# Import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create webdriver object
driver = webdriver.Chrome()

# Get google.co.in
driver.get('https://google.co.in/')
driver.implicitly_wait(30)
my_element = driver.find_element(By.NAME, "q")
my_element.send_keys("Selenium")

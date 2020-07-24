import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\Users\Sam\Documents\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://www.google.com")
print(driver.title)

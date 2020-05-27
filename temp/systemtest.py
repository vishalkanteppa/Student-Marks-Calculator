import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("file:///home/vishal/collage/WT/Student-Marks-Calculator/Site/login.html")
driver.implicitly_wait(100)

time.sleep(3)
driver.close()
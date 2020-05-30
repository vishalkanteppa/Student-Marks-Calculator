import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://google.com")
driver.implicitly_wait(100)

search=driver.find_element_by_name("q")

search.send_keys("idk")

button=driver.find_element_by_name("btnK")
button.click()
# button.send_keys(Keys.ENTER)

time.sleep(3)
driver.close()
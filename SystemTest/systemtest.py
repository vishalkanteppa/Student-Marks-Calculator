import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(
    "file:///home/vishal/collage/WT/Student-Marks-Calculator/Site/login.html")
driver.implicitly_wait(100)

# login page
uname = driver.find_element_by_id("username")
uname.send_keys("sonj")
pwd = driver.find_element_by_id("password")
pwd = pwd.send_keys("sonj")
time.sleep(1)
login = driver.find_element_by_id("Log In")
login.click()

# main page
fname = driver.find_element_by_id("fname")
lname = driver.find_element_by_id("lname")
submit = driver.find_element_by_id("submit")

fname.send_keys("Britney")
lname.send_keys("Spears")
submit.click()
try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(
    ), 'Timed out waiting for PA creation confirmation popup to appear.')
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    print("Alert accepted")
except TimeoutException:
    print("No alert")

fname.clear()
lname.clear()
fname.send_keys("V")
time.sleep(2)
fname.send_keys("ishal")
lname.send_keys("K")
time.sleep(2)
lname.send_keys("anteppa")
submit.click()
time.sleep(2)

pred = driver.find_element_by_id("predict")
pred.click()

# predict page
el = driver.find_element_by_id('sub')
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'Maths':
        option.click()  
        break
marks = driver.find_element_by_id("marks")
marks.send_keys("90")
time.sleep(2)
submit = driver.find_element_by_id("submit")
submit.click()
marks.clear()

el = driver.find_element_by_id('sub')
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'Biology':
        option.click() 
        break
marks.send_keys("92")
time.sleep(2)
submit.click()
time.sleep(2)

perf = driver.find_element_by_id("performance")
perf.click()

# performance page
cat1 = driver.find_element_by_id("cat1")
cat2 = driver.find_element_by_id("cat2")
button = driver.find_element_by_id("button")
button.click()
time.sleep(2)

for option in cat2.find_elements_by_tag_name('option'):
    if option.text == 'Computer Science':
        option.click()  
        break

time.sleep(2)
button.click()
time.sleep(2)

for option in cat1.find_elements_by_tag_name('option'):
    if option.text == 'Biology':
        option.click()  
        break
time.sleep(2)
button.click()
time.sleep(2)

for option in cat2.find_elements_by_tag_name('option'):
    if option.text == 'Chemistry':
        option.click()  
        break
time.sleep(2)
button.click()

for option in cat2.find_elements_by_tag_name('option'):
    if option.text == 'Math':
        option.click()  
        break
time.sleep(2)
button.click()

for option in cat1.find_elements_by_tag_name('option'):
    if option.text == 'Sports':
        option.click()  
        break
time.sleep(2)
button.click()

stud=driver.find_element_by_id("student")
stud.click()

#student page


time.sleep(3)
driver.close()

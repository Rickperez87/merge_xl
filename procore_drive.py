from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

url = 'https://login.procore.com/'
delay=3


driver = webdriver.Chrome('./chromedriver')
driver.get(url)
print(driver.title)

email_login='rperez@wmata.com'
pass_login='_Smashing@123'

procore_username = driver.find_element_by_id('session_email').send_keys(email_login)
procore_password = driver.find_element_by_id('session_password').send_keys(pass_login)
login_btn = driver.find_element_by_id('login-btn').click()

# pkg_b_pulldown = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.Class, 'QHByb')))
pkgb_link=driver.find_element_by_link_text('CRB0020_07 - Dulles Phase 2 WMATA Oversight - Package B').click()
print(pkgb_link)

driver.find_element_by_id('tool-picker-target').click()
# driver.find_element_by_id('tool-item-documents').click()
driver.find_element_by_link_text('Documents').click()
#not working yet below
driver.find_element_by_link_text('1.0 Project Documents').click()
driver.find_element_by_link_text('15 Quality Assurance & Control Records').click()
driver.find_element_by_link_text('15.11 Daily Testing and Inspection Schedule').click()
driver.find_element_by_link_text('Testing and inspections schedules master table').click()

# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)

print(driver.current_url)
time.sleep(15)
driver.close()
driver.close()
driver.quit()
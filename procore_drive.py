from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



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

testing_inspection_url = 'https://app.procore.com/45484/project/documents?folder_id=93300011'

driver.get(testing_inspection_url)

web_element = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[3]/div/div/table/tbody/div[1]/div/div/tr[5]')
hover=ActionChains(driver).move_to_element(web_element)
hover.perform()
driver.find_element_by_xpath()

time.sleep(15)
driver.close()
driver.close()
driver.quit()
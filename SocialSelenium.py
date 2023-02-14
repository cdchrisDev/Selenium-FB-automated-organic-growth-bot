import selenium
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
#from webdriver_manager.firefox import FirefoxDriverManager
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.action_chains import ActionChains 
#import time
#/

#driver = webdriver.Firefox(FirefoxDriverManager().install())
#driver.implicitly_wait(10)


driver = webdriver.Firefox()

driver.get("https://www.facebook.com")

title = driver.title

driver.implicitly_wait(0.5)



#login 

email = "3155347942"
pswd = "Salchipapa123"


emailText=driver.find_element(by=By.NAME, value="email")
emailText.send_keys(email)
passText=driver.find_element(by=By.NAME, value="pass")
passText.send_keys(pswd)
submit_button=driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button.click()
pass

driver.implicitly_wait(3)

#search fan page

#driver.find_element(By.CSS_SELECTOR, '[type="search"]').send_keys("cursero" + Keys.ENTER)

driver.get("https://www.facebook.com/curseroo")



driver.implicitly_wait(1)









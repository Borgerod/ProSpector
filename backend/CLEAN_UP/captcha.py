# # TEMP TEST TEST TEST TEST  
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# from inspect import currentframe, getframeinfo

# def getDriver():
# 	''' gets chrome driver '''
# 	return webdriver.Chrome(options = driverOptions())
# 	# return webdriver.Chrome()

# def driverOptions():
# 	''' selenium settings for opening invisible webdrivers '''
# 	options = webdriver.ChromeOptions()
# 	# options.add_experimental_option("excludeSwitches", ["enable-automation"]) # disable the automation bar [part 1]
# 	# options.add_experimental_option('useAutomationExtension', False) # disable the automation bar [part 2]
# 	# options.add_argument("--headless") # opens window as invisible
# 	# options.add_argument("--disable-gpu") # disable GPU rendering (only software render) 
# 	# options.add_argument('--no-sandbox') # Bypass OS security model	
# 	# options.add_experimental_option('excludeSwitches', ['enable-logging'])  #stops webdriver from printing in console
# 	options.add_experimental_option("detach", True)
# 	return options


# def test():
# 	driver = getDriver()
# 	driver.get("https://www.1881.no/?query=922358982")
# 	# search = driver.find_element("name", "q")
# 	# search.clear()
# 	# search.send_keys(search_term+' maps')
# 	# search.send_keys(Keys.RETURN)

# data_sitekey = {"data-sitekey":"6LewOycTAAAAAOCYwyVA0ntvitZmYh-Wu2Z-uqnT"}


# test()
# # TEMP TEST TEST TEST TEST  




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from solveRecaptcha import solveRecaptcha

browser = webdriver.Chrome()
browser.get('https://www.google.com/recaptcha/api2/demo')

result = solveRecaptcha(
    "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
    "https://www.google.com/recaptcha/api2/demo"
)

code = result['code']

print(code)

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
)

browser.execute_script(
    "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")

browser.find_element(By.ID, "recaptcha-demo-submit").click()

time.sleep(120)
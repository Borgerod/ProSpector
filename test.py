import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import os
import re
import string
import pandas as pd
import numpy as np
from os import path
from tqdm import tqdm
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inspect import currentframe, getframeinfo
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
from tqdm import tqdm
import pandas as pd 
import requests 
from bs4 import BeautifulSoup



''' ___ local imports __________'''
from config import payload, tablenames, settings
from postgres import databaseManager, getInputTable
from file_manager import *
from input_table import inputTable
from base_extractor import genSearchTerm, pullRequest

input_array = getInputTable(tablenames['input'])
print(len(input_array))
output_array = getInputTable(tablenames['output'])
print(len(output_array))


# # Randomization Related
# MIN_RAND        = 0.64
# MAX_RAND        = 1.27
# LONG_MIN_RAND   = 4.78
# LONG_MAX_RAND = 11.1


# # Update this list with proxybroker http://proxybroker.readthedocs.io
# PROXY =[
# {"host": "34.65.217.248", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.15, "error_rate": 0.0},
# {"host": "198.46.160.38", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.36, "error_rate": 0.0},
# {"host": "18.162.100.154", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.62, "error_rate": 0.0},
# {"host": "18.210.69.172", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.22, "error_rate": 0.0},
# {"host": "204.12.202.198", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.3, "error_rate": 0.0},
# {"host": "23.237.100.74", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.32, "error_rate": 0.0},
# {"host": "206.189.192.5", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.63, "error_rate": 0.0},
# {"host": "23.237.173.109", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.4, "error_rate": 0.0},
# {"host": "167.71.83.150", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.41, "error_rate": 0.0},
# {"host": "34.93.171.222", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.92, "error_rate": 0.0},
# {"host": "157.245.67.128", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.61, "error_rate": 0.0},
# {"host": "18.162.89.135", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.71, "error_rate": 0.0},
# {"host": "198.98.55.168", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.65, "error_rate": 0.0},
# {"host": "157.245.124.217", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.7, "error_rate": 0.0},
# {"host": "129.146.181.251", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.76, "error_rate": 0.0},
# {"host": "134.209.188.111", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.78, "error_rate": 0.0},
# {"host": "68.183.191.140", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.82, "error_rate": 0.0},
# {"host": "35.192.138.9", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.29, "error_rate": 0.0},
# {"host": "157.245.207.112", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.85, "error_rate": 0.0},
# {"host": "68.183.191.248", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.87, "error_rate": 0.0},
# {"host": "165.22.54.37", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.88, "error_rate": 0.0},
# {"host": "71.187.28.75", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.34, "error_rate": 0.0},
# {"host": "157.245.205.81", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.92, "error_rate": 0.0},
# {"host": "45.76.255.157", "port": 808, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.45, "error_rate": 0.0},
# {"host": "157.245.197.92", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 1.01, "error_rate": 0.0},
# {"host": "159.203.87.130", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.47, "error_rate": 0.0},
# {"host": "50.195.185.171", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 1.03, "error_rate": 0.0},
# {"host": "144.202.20.56", "port": 808, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.51, "error_rate": 0.0},
# {"host": "157.230.250.116", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 1.14, "error_rate": 0.0},
# {"host": "104.196.70.154", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.64, "error_rate": 0.0}
# ]

# index = int(uniform(0, len(PROXY)))
# PROXY = PROXY[index]["host"]+":"+str(PROXY[index]["port"])


# class SyncMe(unittest.TestCase):

#     number = None
#     headless = False
#     options = None
#     profile = None
#     capabilities = None

#     # Setup options for webdriver
#     def setUpOptions(self):
#         self.options = webdriver.FirefoxOptions()
#         # self.options.add_option('useAutomationExtension', False)
#         self.options.headless = self.headless

#     # Setup profile with buster captcha solver
#     def setUpProfile(self):
#         self.profile = webdriver.FirefoxProfile()
#         self.profile._install_extension("buster_captcha_solver_for_humans-0.7.2-an+fx.xpi", unpack=False)
#         self.profile.set_preference("security.fileuri.strict_origin_policy", False)
#         self.profile.update_preferences()


#     # Enable Marionette, An automation driver for Mozilla's Gecko engine
#     def setUpCapabilities(self):
#         self.capabilities = webdriver.DesiredCapabilities.FIREFOX
#         self.capabilities['marionette'] = True

#     # Setup proxy
#     def setUpProxy(self):
#         self.log(PROXY)
#         self.capabilities['proxy'] = {
#             "proxyType": "MANUAL",
#             "httpProxy": PROXY,
#             "ftpProxy": PROXY,
#             "sslProxy": PROXY
#         }

#     # Setup settings
#     def setUp(self):
#         self.setUpProfile()
#         self.setUpOptions()
#         self.setUpCapabilities()
#         # self.setUpProxy() # comment this line for ignore proxy

#         # On Linux?
#         # https://github.com/mozilla/geckodriver/issues/1756
#         # binary = FirefoxBinary('/usr/lib/firefox-esr/firefox-esr')
#         # self.driver = webdriver.Firefox(options=self.options, capabilities=self.capabilities, firefox_profile=self.profile, executable_path='./geckodriver_linux', firefox_binary=binary)
#         self.driver = webdriver.Firefox(options=self.options, capabilities=self.capabilities, firefox_profile=self.profile, executable_path='./geckodriver_macOS')

#     # Simple logging method
#     def log(s,t=None):
#             now = datetime.now()
#             if t == None :
#                     t = "Main"
#             print ("%s :: %s -> %s " % (str(now), t, s))

#     # Use time.sleep for waiting and uniform for randomizing
#     def wait_between(self, a, b):
#         rand=uniform(a, b)
#         sleep(rand)

#     # Using B-spline for simulate humane like mouse movments
#     def human_like_mouse_move(self, action, start_element):
#         points = [[6, 2], [3, 2],[0, 0], [0, 2]];
#         points = np.array(points)
#         x = points[:,0]
#         y = points[:,1]

#         t = range(len(points))
#         ipl_t = np.linspace(0.0, len(points) - 1, 100)

#         x_tup = si.splrep(t, x, k=1)
#         y_tup = si.splrep(t, y, k=1)

#         x_list = list(x_tup)
#         xl = x.tolist()
#         x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

#         y_list = list(y_tup)
#         yl = y.tolist()
#         y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

#         x_i = si.splev(ipl_t, x_list)
#         y_i = si.splev(ipl_t, y_list)

#         startElement = start_element

#         action.move_to_element(startElement);
#         action.perform();

#         c = 5 # change it for more move
#         i = 0
#         for mouse_x, mouse_y in zip(x_i, y_i):
#             action.move_by_offset(mouse_x,mouse_y);
#             action.perform();
#             self.log("Move mouse to, %s ,%s" % (mouse_x, mouse_y))
#             i += 1
#             if i == c:
#                 break;


#     def do_captcha(self,driver):

#         driver.switch_to.default_content()
#         self.log("Switch to new frame")
#         iframes = driver.find_elements_by_tag_name("iframe")
#         driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])

#         self.log("Wait for recaptcha-anchor")
#         check_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID ,"recaptcha-anchor")))

#         self.log("Wait")
#         self.wait_between(MIN_RAND, MAX_RAND)

#         action =  ActionChains(driver);
#         self.human_like_mouse_move(action, check_box)

#         self.log("Click")
#         check_box.click()

#         self.log("Wait")
#         self.wait_between(MIN_RAND, MAX_RAND)

#         self.log("Mouse movements")
#         action =  ActionChains(driver);
#         self.human_like_mouse_move(action, check_box)

#         self.log("Switch Frame")
#         driver.switch_to.default_content()
#         iframes = driver.find_elements_by_tag_name("iframe")
#         driver.switch_to.frame(iframes[2])

#         self.log("Wait")
#         self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

#         self.log("Find solver button")
#         capt_btn = WebDriverWait(driver, 50).until(
#                 EC.element_to_be_clickable((By.XPATH ,'//button[@id="solver-button"]'))
#                 )

#         self.log("Wait")
#         self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

#         self.log("Click")
#         capt_btn.click()

#         self.log("Wait")
#         self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

#         try:
#             self.log("Alert exists")
#             alert_handler = WebDriverWait(driver, 20).until(
#                     EC.alert_is_present()
#                     )
#             alert = driver.switch_to.alert
#             self.log("Wait before accept alert")
#             self.wait_between(MIN_RAND, MAX_RAND)

#             alert.accept()

#             self.wait_between(MIN_RAND, MAX_RAND)
#             self.log("Alert accepted, retry captcha solver")

#             self.do_captcha(driver)
#         except:
#             self.log("No alert")


#         self.log("Wait")
#         driver.implicitly_wait(5)
#         self.log("Switch")
#         driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])


#     # Main function
#     def test_run(self):
#         driver = self.driver
#         number = self.number

#         self.log("Start get")
#         driver.get('https://sync.me')
#         self.log("End get")

#         self.log("Send phone")

#         # sync.me seems to have moved away from IDs
#         # phone_input = driver.find_element_by_xpath('//*[@id="mobile-number"]')
#         phone_input = driver.find_element_by_xpath('//input[@placeholder="Search any phone number"]')
#         phone_input.send_keys(number)

#         self.log("Wait")
#         self.wait_between(MIN_RAND, MAX_RAND)

#         search_btn = WebDriverWait(driver, 20).until(
#                 # EC.presence_of_element_located((By.ID ,"submit"))
#                 EC.presence_of_element_located((By.XPATH, '//button[contains(@class, "SearchNumber_searchNumber__find")]'))
#                 )

#         self.log("Wait")
#         self.wait_between(MIN_RAND, MAX_RAND)
#         search_btn.click()

#         self.log("Wait")
#         self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)


#         self.do_captcha(driver)

#         self.log("Done")


#     def tearDown(self):
#         self.wait_between(21.13, 31.05)

# if __name__ == "__main__":
#     if len(sys.argv) > 0:
#         SyncMe.number = sys.argv.pop()
#     else:
#         print("Must have number to check")
#         exit(0)
#     unittest.main()


# # from selenium import webdriver
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support import expected_conditions as exp_con
# # from reCaptchaBypasser import GoogleCaptchaV2 #reCaptchaV2Scraper
# # from time import sleep

# # driver = webdriver.Firefox(executable_path=r"./geckodriver")

# # driver.get("https://google.com/recaptcha/api2/demo")

# # captcha_bypasser = reCaptchaV2Scraper(driver, 4)
# # res = captcha_bypasser.reCaptchaGoogleV2()
# # if res != None:
# #     if res["Status"] == True:
# #         print(f"Bypassed !!! | rCaptcha Audio Text : {res['reCaptchaText']}")
# #         sleep(2)
# #         submit_btn = WebDriverWait(driver, timeout=4).until(exp_con.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
# #         submit_btn.click()
# #         print("Submited !!!")
# #     elif res["Status"] == False:
# #         print("Cannot Bypass reCaptcha !!!")



# # import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
# # import pandas as pd 
# # import requests 
# # from bs4 import BeautifulSoup
# # import numpy as np
# # import pandas as pd 
# # import json
# # import psycopg2
# # from psycopg2.extras import Json
# # from sqlalchemy import create_engine
# # import concurrent.futures
# # from tqdm import tqdm
# # import gzip
# # import pprint
# # import ast

# # # ___ local imports __________
# # from config import payload, tablenames, settings
# # from postgres import databaseManager, cleanUp, fetchData, checkForTable, postLastUpdate, replacetData
# # from file_manager import *
# # import os 


# # # def myfunc(a,b, **kwargs):
# # #       c = kwargs.get('c', None)
# # #       d = kwargs.get('d', None)n
# # #       print(a,b,c,d)


# # # a, b = 'marie','cat'  
# # # myfunc(a,b, c='nick', d='dog',)



# # # df = fetchData('gulsesider_test_table')
# # # all_true = df.query('betalt_oppføring == True')
# # # print(all_true)
# # # print(fetchData('gulsesider_test_table'))
# # # print(os.cpu_count() or 1)
# # # def extractionManager(chunk):
# # # 	return chunk


# # # input_array = fetchData('input_table').to_numpy()
# # # print(f'full input_array: {len(input_array)}')
# # # chunks = input_array
# # # # chunks = input_array[:600] #TEMP - while testing
# # # print(f'current run uses {len(chunks)}')
# # # print(f'current run uses {len(chunks[0])}')
# # # print(f'example; first element in the first chunk: {chunks[0][0]}')
# # # with concurrent.futures.ThreadPoolExecutor() as executor:
# # # # with concurrent.futures.ThreadPoolExecutor(max_workers=-1) as executor:
# # # 	results = executor.map(extractionManager, chunks)

# # '''! DONT DELETE THIS _________________________________________________________
# # '''

# # # '''BOILERPLATE CODE FOR input_table updater
# # # '''

# # # ''' liste 1 original'''
# # # # lst1 = [[98908098, 'company1', 10],
# # # # [55508098, 'company2', 20],
# # # # [95454008, 'company3', 30],
# # # # [92228098, 'company4', 40],]


# # # ''' liste 1 men med slettet enhet'''
# # # lst1 = [[98908098, 'company1', 10],
# # # [55508098, 'company2', 20],
# # # [95454008, 'company3', 30],
# # # [92228098, 'company4', 40],]
# # # # _____________________________________

# # # ''' liste 2 original'''
# # # # lst2 = [[98908098, 'company1', 10],
# # # # [55508098, 'company2', 666],
# # # # [95454008, 'company3', 666],
# # # # [92228098, 'company4', 40],]

# # # # ''' liste 2 men med slettet enhet'''
# # # lst2 = [[98908098, 'company1', 10],
# # # [55508098, 'company2', 666],
# # # [95454008, 'company3', 666],
# # # [66255098, 'company5', 50],]

# # # # # ''' liste 2 men med ny enhet'''
# # # # lst2 = [[98908098, 'company1', 10],
# # # # [55508098, 'company2', 666],
# # # # [95454008, 'company3', 666],
# # # # [92228098, 'company4', 40],
# # # # [66255098, 'company5', 50],]
# # # # _____________________________________


# # # df1 = pd.DataFrame(lst1, columns=['org_num', 'company_name', 'value'])
# # # print(df1)
# # # df2 = pd.DataFrame(lst2, columns=['org_num', 'company_name', 'value'])
# # # print(df2)
# # # print()
# # # print()
# # # ''' 

# # # '''
# # # common = df1.merge(df2,on=['org_num','company_name'])
# # # print(common)

# # # deleted = df1[(~df1.org_num.isin(common.org_num))&(~df1.company_name.isin(common.company_name))]
# # # print(df)

# # # new = df2[~(df1.org_num.isin(df2.org_num))&(~df1.company_name.isin(df2.company_name))]
# # # print(df)



# # # '''
# # #     makes a dataframe from all differences
# # # '''


# # # # df = pd.concat([df1, df2])
# # # # df = df.reset_index(drop = True)

# # # # df_gpby = df.groupby(list(df.columns))

# # # # idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]

# # # # df = df.reindex(idx)
# # # # print(df)
# # # # df = df.drop_duplicates(subset = 'org_num', keep = 'last')
# # # # print(df)


# # '''! _____________________________________________________________________________________________
# # '''

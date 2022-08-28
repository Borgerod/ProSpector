import csv
from time import sleep, time
from random import uniform, randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

import re, csv
from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException    
import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import re
import logging
import pandas as pd
import numpy as np
from tqdm import tqdm
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from inspect import currentframe, getframeinfo
import os
import pickle 


def write_stat(loops, _time):
    with open("stat.csv", "a", newline="") as csvfile:
        spam_writer = csv.writer(
            csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        spam_writer.writerow([loops, _time])


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def wait_between(a, b):
    rand = uniform(a, b)
    sleep(rand)


def dimention(driver):
    d = int(
        driver.find_element_by_xpath(
            '//div[@id="rc-imageselect-target"]/table'
        ).get_attribute("class")[-1]
    )
    return d if d else 3  # dimention is 3 by default


# ***** main procedure to identify and submit picture solution
def solve_images(driver):
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "rc-imageselect-target"))
    )
    dim = dimention(driver)
    # ****************** check if there is a clicked tile ******************
    if check_exists_by_xpath(
        driver,
        '//div[@id="rc-imageselect-target"]/table/tbody/tr/td[@class="rc-imageselect-tileselected"]',
    ):
        rand2 = 0
    else:
        rand2 = 1

    # wait before click on tiles
    wait_between(0.5, 1.0)
    # ****************** click on a tile ******************
    tile1 = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (
                By.XPATH,
                '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(
                    randint(1, dim), randint(1, dim)
                ),
            )
        )
    )
    tile1.click()
    if rand2:
        try:
            driver.find_element_by_xpath(
                '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(
                    randint(1, dim), randint(1, dim)
                )
            ).click()
        except NoSuchElementException:
            print("\n\r No Such Element Exception for finding 2nd tile")

    # ****************** click on submit buttion ******************
    driver.find_element_by_id("recaptcha-verify-button").click()


# start = time()


def resolve(driver):
    main_win = driver.current_window_handle

    driver.switch_to.default_content()

    # *************  locate first iframe  **************
    # iframe1 = WebDriverWait(driver, 0.5).until(
    #     ec.presence_of_element_located((By.ID, "main-iframe"))
    # )
    iframe1 = WebDriverWait(driver, 20).until(
        ec.presence_of_element_located((By.ID, "main-iframe"))
    )
    # move the driver to the first iFrame
    driver.switch_to.frame(iframe1)

    # *************  locate second iframe  **************
    iframe2 = WebDriverWait(driver, 0.5).until(
        ec.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "iframe[name*='a-'][src*='https://www.google.com/recaptcha/api2/anchor?']",
            )
        )
    )

    # move the driver to the second iFrame
    driver.switch_to.frame(iframe2)

    # *************  locate CheckBox  **************
    check_box = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "recaptcha-anchor"))
    )

    # *************  click CheckBox  ***************
    wait_between(0.5, 0.7)
    # making click on captcha CheckBox
    check_box.click()

    # ***************** back to main window **************************************
    driver.switch_to.window(main_win)

    wait_between(2.0, 2.5)

    # move the driver to the first iFrame
    driver.switch_to.frame(iframe1)

    # *************  locate the popup's iframe  **************
    iframe_popup = WebDriverWait(driver, 0.5).until(
        ec.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                 "iframe[title*='recaptcha challenge'][src*='https://www.google.com/recaptcha/api2/bframe?']",
            )
        )
    )

    i = 1
    while i < 130:
        print("\n\r{0}-th loop".format(i))
        # ******** check if checkbox is checked at the 1st frame ***********
        driver.switch_to.window(main_win)
        WebDriverWait(driver, 10).until(
            ec.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
        )
        wait_between(1.0, 2.0)
        if check_exists_by_xpath(driver, '//span[@aria-checked="true"]'):
            write_stat(i, round(time() - start) - 1)  # saving results into stat file
            break

        driver.switch_to.window(main_win)

        wait_between(0.3, 1.5)

        # move the driver to the first iFrame
        driver.switch_to.frame(iframe1)

        # ********** To the second frame to solve pictures *************
        driver.switch_to.frame(iframe_popup)
        solve_images(driver)
        i = i + 1

def driverOptions():
    ''' selenium settings for opening invisible webdrivers '''
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # disable the automation bar [part 1]
    options.add_experimental_option('useAutomationExtension', False) # disable the automation bar [part 2]
    options.add_argument("window-size=1920,1080")
    # options.add_argument("--headless") # opens window as invisible
    options.add_argument("--disable-gpu") # disable GPU rendering (only software render) 
    options.add_argument('--no-sandbox') # Bypass OS security model 
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  #stops webdriver from printing in console
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')

    # options.add_argument(f'--user-agent="{UserAgent().random}"')
    # options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
    return options


def getDriver():
    ''' gets chrome driver '''
    return webdriver.Chrome(options = driverOptions())


driver = getDriver()
driver.get('https://www.google.com/search?q=UNNS%20NEGLDESIGN%20UNN%20K%20SIGVARTSEN%20maps')
# time.sleep(2)
resolve(driver)
# mainWin = driver.current_window_handle  #* CATCHPA SOLVER
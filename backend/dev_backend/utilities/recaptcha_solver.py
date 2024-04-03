
import time; START = time.perf_counter() #Since it also takes time to Import libs, I allways START the timer asap. 
from time import sleep
import csv
from random import uniform, randint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Recaptcha:

    def write_stat(self, loops: int, time: int):
        with open('stat.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([loops, time])  	 
        
    def check_exists_by_xpath(self, xpath, driver) -> bool:
        ''' #! NOTABLE CHANGE: added the "driver" param, if any future errrs should occour check here first. 
        '''
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
        
    def wait_between(self, a: float, b: float) -> None:
        rand = uniform(a, b) 
        sleep(rand)

    def dimention(self, driver: webdriver) -> int: 
        '''
            dimention is 3 by default
        '''
        d = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table').get_attribute("class")[-1])
        # d = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table').get_attribute("class")[-1]); #! Litt usikker på hvorfor den hadde";" endret men ikke fjernet
        return d if d else 3
        
    def solver(self, driver: webdriver):
        mainWin = driver.current_window_handle  
        driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])

        '''  
            locate CheckBox  
        '''
        CheckBox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))
                ) 

        '''
            click CheckBox
        '''
        self.wait_between(0.5, 0.7)  
        CheckBox.click() 
        

        '''
            back to main window
        '''
        driver.switch_to_window(mainWin)  

        self.wait_between(2.0, 2.5) 
        '''
            switch to the second iframe by tag name
        '''
        driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1])  
        i = 1
        while i < 130:
            print('\n\r{0}-th loop'.format(i))
            '''
                check if checkbox is checked at the 1st frame
            '''
            driver.switch_to_window(mainWin)   
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME , 'iframe'))
                )  
            self.wait_between(1.0, 2.0)
            '''
                saving results into stat file
            '''
            if self.check_exists_by_xpath('//span[@aria-checked="true"]', driver): 
                import winsound
                winsound.Beep(400,1500)
                self.write_stat(i, round(time()-START) - 1 )
                break 
                
            driver.switch_to_window(mainWin)   
            
            '''
                To the second frame to solve pictures
            '''
            self.wait_between(0.3, 1.5) 
            driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1]) 
            self.solve_images(driver)
            i = i + 1
        
    def solve_images(self, driver: webdriver): 
        '''
            main procedure to identify and submit picture solution
        '''	
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID ,"rc-imageselect-target"))
            ) 		
        dim = self.dimention(driver)	

        '''
            check if there is a clicked tile
        '''
        if self.check_exists_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr/td[@class="rc-imageselect-tileselected"]', driver):
            rand2 = 0
        else:  
            rand2 = 1 	 

        ''' 
            wait before click on tiles, then clicks on a tile  
        '''
        self.wait_between(0.5, 1.0)
        tile1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH ,   '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim )))
                ) 
            )   
        tile1.click() 
        if (rand2):
            try:
                driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim))).click()
            except NoSuchElementException:          		
                print('\n\r No Such Element Exception for finding 2nd tile')
        
        '''
            click on submit buttion 
        ''' 
        driver.find_element_by_id("recaptcha-verify-button").click()

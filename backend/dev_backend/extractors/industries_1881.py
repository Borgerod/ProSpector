
import json
import string
from bs4 import BeautifulSoup
import requests
from requests.models import Response as response #annotaions
from bs4 import element

from backend.dev_backend.SQL.models.insert import Insert
from backend.dev_backend.SQL.reset import Reset #annotaions


''' 
____ Track_record ____
	tot. time:  3.590s  
'''

class Industry1881Extractor:

    def __init__(self) -> None:
        self.base_url = "https://www.1881.no/sitemap/industries-"
        self.headers = self.getHeaders
        self.urls = self.genUrlsByLetters
        self.url = None
        self.industries = None
        self.category_hits = None
   
    @property
    def getHeaders(self) -> dict:
        return {
                "cookie": "__uzma=e69d520f-a8db-46ec-b5d1-7d2e26930e28; __uzmc=163051371814; __uzmb=1668010547; __uzmd=1668010570; captletteresponse=1; Expires=null; Path=/; Domain=www.1881.no",
                "authority": "cdn.pbstck.com",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "origin": "https://www.1881.no",
                "pragma": "no-cache",
                "referer": "https://www.1881.no/sitemap/industries-a/",
                "sec-ch-ua": "^\^Google",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "^\^Windows^^",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
            }
    
    @property
    def genUrlsByLetters(self) -> list[str]:
        return [
            f"{self.base_url}{letter}" for letter #builds list of urls by..            
            in list(string.ascii_lowercase) + ['æ','ø','å'] # ..letters from the alphabes
            ] 

    def getReq(self) -> response:
        return requests.request("GET", self.url, headers = self.getHeaders)
    
    def parseData(self) -> list[str] or None:
        soup = BeautifulSoup(self.getReq().text, "html.parser")
        print(soup.text)
        wrapper = soup.find('ul', class_ = "list-columns list-columns--3")
        try:
            rows = wrapper.find_all('a', href = True)
            return [a.text.lower() for a in rows]
        except AttributeError:
            return []
    
    def stringCleaner(self, indudtries_by_letter) -> list[str] or None:
        '''
        replacing and removes characters that would raise an error as url
        '''
        edited_ind_for_letter = []
        for ind in indudtries_by_letter:
            dash_fix = ind.replace(" ", "-").replace("---","-").replace("--","-")           #converts multiple dashes to single
            parenth_fix = dash_fix.replace("(", "").replace(")", "")                        #removes parentheses
            øæå_fix = parenth_fix.replace("ø", "oe").replace("æ", "ae").replace("å", "aa")  #converts norwegian alphabet to english
            edited_ind_for_letter.append(øæå_fix)
        return edited_ind_for_letter

    def getListFromPage(self) -> list[str] or None:
        '''
        gets list of industries_by_letter, then returns cleaned list
        '''
        return self.stringCleaner(self.parseData()) # industries_by_letter => url_ready_strings

    def fetchIndustries(self) -> None:
        ''' NOTE: Insert <- list[str]
        extracts list of industries from alphabetical sorted lists on 1881.no,
        then cleans up the strings ("url_ready_strings"), then insert to db. 
        '''
        Reset().Industry1881()
        for self.url in self.urls:
            for industry in self.getListFromPage():
                Insert().to1881Industries(dataset = industry)


    # @property
    # def genUrlsByLetters(self) -> list[str]:
    #     ''' builds a list of urls, based on letters from the alphabet '''
    #     return [f"{self.base_url}{letter}" for letter in list(string.ascii_lowercase) + ['æ','ø','å']] 
    

    # def fetchIndustries(self) -> None:
    #     ''' NOTE: Insert <- list[str]

    #     fetches a list of industries for each letteracter in the alphabet ("industries_by_letter")
    #     then cleans up the strings ("url_ready_strings"), then insert to db. 
    #     '''
    #     Reset().Industry1881()
    #     for url in self.urls:
    #         response = requests.request("GET", url, headers = self.getHeaders())
    #         soup = BeautifulSoup(response.text, "html.parser")
    #         industries_by_letter = self.parseData(soup)
    #         url_ready_strings = self.stringCleaner(industries_by_letter)
    #         for industry in url_ready_strings:
    #             Insert().to1881Industries(dataset = industry)



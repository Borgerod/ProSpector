
import string
import requests
from requests.models import Response as response #annotaions
from bs4 import BeautifulSoup
from bs4 import element #annotaions
from multiprocessing import Pool
from tqdm import tqdm

''' ___ Local Imports ___ '''
from SQL.insert import Insert
from SQL.reset import Reset


''' 
____ Track_record ____
	tot. time:  5.050s 
'''


'''
NOTE: How "categories" differs from "bransjer_proff" & "bransjer_1881"
    since CategoryExtractor spent 3x more time than the others, it uses multi threading

    due to limitations from Pool, url will be used a parameter, 
    and be set as a state in insertListFromPageToDb() instead.
'''

class CategoryExtractor:

    def __init__(self) -> None:
        self.base_url = "https://www.gulesider.no/bedriftsregister/kategorier-"
        self.headers = self.getHeaders
        self.urls = self.genUrlsByLetters
        self.url = None
        
    @property
    def getHeaders(self) -> dict:
        return {
            "cookie": "_hjSessionUser_1569514=eyJpZCI6ImZjZGEyYWI0LWFlMGMtNWQxMS1hOTZiLTdlNDQwZWUxYmRmYiIsImNyZWF0ZWQiOjE2NTY2NzM5NDE5MzgsImV4aXN0aW5nIjp0cnVlfQ==; euconsent-v2=CPhHQPEPhHQPEAKAXBNOClCgAAAAAH_AABpwAAARvABIFS4gAbAoMCSAAIgEQIgrAAIAUAEAAACBAAAAAAAQAgEqAIAAAAAAAABAAwBQAQCAAAAAAAAAAAAgQAAACAAAAAAAAAAAEAAIIACgMAgABAJAAAAgAACAgAACAABAAAgACAAgIAAoAJBTCAAEAAAABCQEACAAAAAAAAAgMAQAACRAQQAAAAAAAAAAAAQAAAAA.YAAAAAAAAAAA; _pa=PA2.0370463469796563; JSESSIONID=D83F04B5C695B4C327334C5C247C2B6F; _gid=GA1.2.1949323138.1667834959; _pk_ses.2.d737=1; ln_or=d; _pk_id.2.d737=84b3886ac0cec608.1667313613.2.1667835574.1667834959.; _ga=GA1.2.810621682.1666167700; _gat=1; _ga_JKQ3JPCECD=GS1.1.1667834959.12.1.1667835718.0.0.0; AWSALB=gnCHn+q27D1uOnOaLty8yUB9fZc1Ngnx7BsLvpfoLKsOzQIq70b0V7Yik2veJEpg/xoDqI55hS+9S37Jk70Xdk51ptQX5kCzpAtnKsmGO2zHnsC3SxYROxaIsLGK; AWSALBCORS=gnCHn+q27D1uOnOaLty8yUB9fZc1Ngnx7BsLvpfoLKsOzQIq70b0V7Yik2veJEpg/xoDqI55hS+9S37Jk70Xdk51ptQX5kCzpAtnKsmGO2zHnsC3SxYROxaIsLGK",
            "authority": "proff.no",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://www.gulesider.no/",
            "sec-ch-ua": "^\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
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
    
    def parseData(self) -> element:
        soup = BeautifulSoup(self.getReq().text, "html.parser")
        return soup.find('div', class_ = "MuiGrid-root MuiGrid-container css-v3z1wi")

    def insertListFromPageToDb(self, url:str):
        ''' NOTE: Insert <- list[str]
        '''
        self.url = url 
        for category in self.parseData().find_all('a', href = True):
            Insert().toCategories(category.text)

    def fetchCategories(self) -> None:
        '''
        extracts industries from alphabetical sorted lists on gulesider.no
        '''
        Reset().categories()
        with Pool() as pool:
            list(tqdm(pool.imap_unordered(self.insertListFromPageToDb, self.urls), total = len(self.urls)))


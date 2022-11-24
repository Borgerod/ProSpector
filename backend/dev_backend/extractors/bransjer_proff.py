
import string
import requests
from requests.models import Response as response #annotaions

from bs4 import BeautifulSoup
from bs4 import element #annotaions

''' ___ Local Imports ___ '''
from SQL.insert import Insert


''' 
____ Track_record ____
	tot. time:  5.510s 
'''
class IndustryProffExtractor:

    def __init__(self) -> None:
        self.base_url = "https://proff.no/industry/select?beginLetter="
        self.urls = self.getUrls
        self.headers = self.getHeaders
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
            "referer": "https://proff.no/s^%^C3^%^B8k-etter-bransje/adresseringsleverand^%^C3^%^B8rer/I:10159/?q=Adresseringsleverand^%^C3^%^B8rer",
            "sec-ch-ua": "^\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }

    @property
    def getChars(self) -> list[str]:
        ''' returns the alphabet as a list '''
        return list(string.ascii_lowercase) + ['æ','ø','å']  
    
    @property
    def getUrls(self) -> list[str]:
        ''' builds a list of urls, based on letters from the alphabet '''
        return [self.base_url+char for char in self.getChars]
    
    @property
    def getReq(self) -> response:
        return requests.request("GET", self.url, headers = self.getHeaders)
    
    @property
    def parseData(self) -> element:
        soup = BeautifulSoup(self.getReq.text, "html.parser")
        return soup.find('ul', class_ = "three-aligned-columns clear")

    def getListFromPage(self) -> list[str]:
        return self.parseData.find_all('a', href = True)

    def fetchIndustries(self) -> None:
        '''extracts industries from alphabetical sorted lists on proff.no'''
        for self.url in self.urls:
            for industry in self.getListFromPage():
                Insert().toProffIndustries(industry.text)
                
if __name__ == '__main__':
    IndustryProffExtractor().fetchIndustries()

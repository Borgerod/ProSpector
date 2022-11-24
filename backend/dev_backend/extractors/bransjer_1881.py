
import json
import string
from bs4 import BeautifulSoup
import requests

from SQL.insert import Insert
from SQL.reset import Reset


''' 
____ Track_record ____
	tot. time:  3.590s  
'''

class Industry1881Extractor:

    def __init__(self) -> None:
        self.urls = self.getUrls
        self.headers = self.getHeaders
        self.industries = None
        self.category_hits = None

    def urlBuilder(self, char):
        return f"https://www.1881.no/sitemap/bransjer-{char}/"

    def getChars(self) -> list[str]:
        return list(string.ascii_lowercase) + ['æ','ø','å']  # returns the alphabet as a list 
    
    @property
    def getUrls(self) -> list[str]:
        chars = self.getChars()
        return [self.urlBuilder(char) for char in chars]
    
    def getHeaders(self) -> dict:
        return {
                "cookie": "__uzma=e69d520f-a8db-46ec-b5d1-7d2e26930e28; __uzmc=163051371814; __uzmb=1668010547; __uzmd=1668010570;captchaResponse=1; Expires=null; Path=/; Domain=www.1881.no",
                "authority": "cdn.pbstck.com",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "origin": "https://www.1881.no",
                "pragma": "no-cache",
                "referer": "https://www.1881.no/sitemap/bransjer-a/",
                "sec-ch-ua": "^\^Google",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "^\^Windows^^",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
            }
   
    def parseData(self, soup):
        wrapper = soup.find('ul', class_ = "list-columns list-columns--3")
        try:
            rows = wrapper.find_all('a', href = True)
            return [a.text.lower() for a in rows]
        except AttributeError:
            return []
    
    def editIndustryList(self, industries_for_char):
        edited_ind_for_char = []
        for ind in industries_for_char:
            dashFix = ind.replace(" ", "-").replace("---","-").replace("--","-")
            parenthFix = dashFix.replace("(", "").replace(")", "")
            øæåFix = parenthFix.replace("ø", "oe").replace("æ", "ae").replace("å", "aa")
            edited_ind_for_char.append(øæåFix)
        return edited_ind_for_char



    def genIndustriesList(self, data):
        industries_for_char = []
        for item in data:
            industries_for_char.append(item['label'])
        return industries_for_char

    def fetchIndustries(self):
        Reset().Industry1881()
        for url in self.urls:
            response = requests.request("GET", url, headers = self.getHeaders())
            soup = BeautifulSoup(response.text, "html.parser")
            industries_for_char = self.parseData(soup)
            edited_ind_for_char = self.editIndustryList(industries_for_char)
            Insert().to1881Industries(dataset = edited_ind_for_char)
   


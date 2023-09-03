import json
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from multiprocessing import Pool
import requests
from tqdm import tqdm

from SQL.reset import Reset
from extractors.industries_gulesider import IndustryGulesiderExtractor

from pprint import pprint 


''' 
____ Track_record ____
    tot. time:  178.880s  (2.981m)

'''

def	throwTracker(throws):
    '''
    keeps track of all thrown businesses
    '''
    # todo: make throwTracker
    throwTracker.counter += throws

class GulesiderExtractor:
    def __init__(self) -> None:
        self.url = None
    
    @property
    def payload(self)-> dict:
        return ""

    @property 
    def headers(self, ) -> dict:
        return {
            "cookie": "55f7017582a6e57bfac34dfdb9e53ef4=bfd07396204ae4f716e14551443c489f; __cf_bm=uJGEek.z0nnqxfAGE1VkCGeiirS9E5XWsD6A2hxCe.E-1693411819-0-AcMKCabGKspyKkCKeqCE%2B9ohd0wCx1gM502wN8MEfQJbMb9HZsMWW16y8MBNufXTgolMJqK4BsV0xTwU4NjHsNY%3D",
            "User-Agent": "Insomnia/2023.5.3"
        }
    def getData(self, url:str) -> dict:
        '''
        __idea__
        for i in category:
            spawn threads that goes through each page_num

        NOTE: alot of companies has probobly multiple industries and will show up multiple times
        '''	        
        response = requests.request("GET", url, data=self.payload, headers=self.headers)
        script = BeautifulSoup(response.content, "html.parser").find('script', id = "__NEXT_DATA__")
        return json.loads(script.text.replace('\u2665',''))
     
    def get_industries(self, urls):
        industries = []
        page_counter = 0 
        for url in urls:
            for industry in self.getData(url)['props']['pageProps']['categories']['categories']:
                industries.append(industry['label'])
                page_counter += industry['hits']
        return industries, page_counter
  

def main():
    categories = ['https://www.gulesider.no/bedriftsregister/kategorier-a', 'https://www.gulesider.no/bedriftsregister/kategorier-b', 'https://www.gulesider.no/bedriftsregister/kategorier-c', 'https://www.gulesider.no/bedriftsregister/kategorier-d', 'https://www.gulesider.no/bedriftsregister/kategorier-e', 'https://www.gulesider.no/bedriftsregister/kategorier-f', 'https://www.gulesider.no/bedriftsregister/kategorier-g', 'https://www.gulesider.no/bedriftsregister/kategorier-h', 'https://www.gulesider.no/bedriftsregister/kategorier-i', 'https://www.gulesider.no/bedriftsregister/kategorier-j', 'https://www.gulesider.no/bedriftsregister/kategorier-k', 'https://www.gulesider.no/bedriftsregister/kategorier-l', 'https://www.gulesider.no/bedriftsregister/kategorier-m', 'https://www.gulesider.no/bedriftsregister/kategorier-n', 'https://www.gulesider.no/bedriftsregister/kategorier-o', 'https://www.gulesider.no/bedriftsregister/kategorier-p', 'https://www.gulesider.no/bedriftsregister/kategorier-q', 'https://www.gulesider.no/bedriftsregister/kategorier-r', 'https://www.gulesider.no/bedriftsregister/kategorier-s', 'https://www.gulesider.no/bedriftsregister/kategorier-t', 'https://www.gulesider.no/bedriftsregister/kategorier-u', 'https://www.gulesider.no/bedriftsregister/kategorier-v', 'https://www.gulesider.no/bedriftsregister/kategorier-w', 'https://www.gulesider.no/bedriftsregister/kategorier-x', 'https://www.gulesider.no/bedriftsregister/kategorier-y', 'https://www.gulesider.no/bedriftsregister/kategorier-z', 'https://www.gulesider.no/bedriftsregister/kategorier-æ', 'https://www.gulesider.no/bedriftsregister/kategorier-ø', 'https://www.gulesider.no/bedriftsregister/kategorier-å']
    industries, page_counter = GulesiderExtractor().get_industries(categories)
    print(f"""
        tot amount of industries: {len(industries)}
        industries examples [20:25]: {industries[20:25]}
        tot amount of pages to scrape: {f'{page_counter:,}'.replace(',', " ")}
        """)
    
if __name__ == '__main__':
    main()
    
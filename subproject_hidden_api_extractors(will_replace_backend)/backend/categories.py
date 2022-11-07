
import json
import string
import requests

# ___ Local Imports ___
from SQL.insert import Insert


class CategoryExtractor:

    def __init__(self) -> None:
        self.urls = self.getUrls
        self.headers = self.getHeaders
        self.categories = None
        self.category_hits = None
        # self.hitCounter.counter = 0
        
    def urlBuilder(self, char):
        return f"https://www.gulesider.no/_next/data/338IdBW7dht2IHQ27Ay-p/nb/catalogue/category/{char}.json"

    def getChars(self) -> list[str]:
        return list(string.ascii_lowercase) + ['æ','ø','å']  # returns the alphabet as a list 
    
    @property
    def getUrls(self) -> list[str]:
        chars = self.getChars()
        return [self.urlBuilder(char) for char in chars]
    
    def getHeaders(self) -> dict:
        return {
            "cookie": "55f7017582a6e57bfac34dfdb9e53ef4=e574a075ef616796844969c19a9ddd18",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Cookie": "_hjSessionUser_2847992=eyJpZCI6ImE5ZGVjM2Q1LTZjZGYtNWY0ZC1iODExLTYwYzg3YTg1NzQ4ZCIsImNyZWF0ZWQiOjE2NTY2NzU3MTQyMTIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_1215995=eyJpZCI6IjBlZWRlYzcwLThiNDAtNWMxMS1iZjI0LWY3MTM0MjU5NmNjOCIsImNyZWF0ZWQiOjE2NTcxMjIyMDM1MjEsImV4aXN0aW5nIjp0cnVlfQ==; addtl_consent=1~; _enid=sm6dp3v4zv2nwh0fe75jh4626c6s30ogjsz9j49r; _dcid=dcid.1.1666388828330.100705442; euconsent-v2=CPhMsoAPhMsoAAKAsANOCmCgAAAAAH_AABpwAAASIAJMNW4gC7MscGTQMIoEQIwrCQqgUAEFAMLRAYAODgp2VgEuoIEACAUARgRAgwBRgQCAAASAJCIAJACwQAAAiAQAAgARAIQAMDAILACwMAgABANAxACgAECQgyICIpTAgKgSCA1sqEEoKpDTCAOssAKARGRUACIJAQSAAICwcAwBICViwQJMUL5ACMEKAUQAAAIAAAAA.YAAAAAAAAAAA; _cmpRepromptHash=CPhMsoAPhMsoAAKAsANOCmCgAAAAAH_AABpwAAASIAJMNW4gC7MscGTQMIoEQIwrCQqgUAEFAMLRAYAODgp2VgEuoIEACAUARgRAgwBRgQCAAASAJCIAJACwQAAAiAQAAgARAIQAMDAILACwMAgABANAxACgAECQgyICIpTAgKgSCA1sqEEoKpDTCAOssAKARGRUACIJAQSAAICwcAwBICViwQJMUL5ACMEKAUQAAAIAAAAA.YAAAAAAAAAAA.1.KTvSi1ifP7BGbdpiCttXPA==; 55f7017582a6e57bfac34dfdb9e53ef4=bd507cea0a5f1a0a309cc12fc95d926b; _ensess=1x6rz9iksc9ac999tfau; yextversion=yext-external-a; s_cc=true; s_uuid=a0fmba8hzkwxlenv; s_sq=^%^5B^%^5BB^%^5D^%^5D",
            "Pragma": "no-cache",
            "Referer": "https://www.gulesider.no/bedriftsregister",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "sec-ch-ua": "^\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^"
        }
    # ! OLD
    # def parseData(self, json_res:json):
    #     data = json_res['pageProps']['categoriesList']['categories']
    #     categories_for_char = []
    #     # category_hits ""= [] #>could be useful 
    #     for item in data:
    #         categories_for_char.append(item['label'])
    #         # category_hits.appen(item['hits']) #>could be useful 
    #     return categories_for_char#, category_hits #>could be useful 
    
    #* NEW 
    def parseData(self, json_res:json):
        # data = 
        return json_res['pageProps']['categoriesList']['categories']
    
    #* NEW 
    def genCategoriesList(self, data):
        categories_for_char = []
        for item in data:
            categories_for_char.append(item['label'])
        return categories_for_char
    
    #* NEW 
    def genHitList(self, data):
        category_hits = []
        for item in data:
            category_hits.append(item['hits'])
        return category_hits

    #* NEW        
    # @property
    # def getCategories(self):

    def fetchCategories(self):
        # total_categories = []
        for url in self.urls:
            json_res = requests.request("GET", url, headers=self.getHeaders()).json()
            data = self.parseData(json_res)
            categories_for_char = self.genCategoriesList(data)
            hitCounter(sum(self.genHitList(data)))
            Insert().toCategories(dataset=categories_for_char)
            # total_categories += categories_for_char 
        # print(f"total hits for all categories: {hitCounter.counter}")
        # return total_categories

    #* NEW        
    @property
    def getHits(self):
        category_hits = []
        for url in self.urls:
            json_res = requests.request("GET", url, headers=self.getHeaders()).json()
            data = self.parseData(json_res)
            hits_for_char = self.genHitList(data)
            hitCounter(sum(hits_for_char))
            category_hits += hits_for_char
        return category_hits

def hitCounter(hits):
    hitCounter.counter += hits



hitCounter.counter = 0
# categories = CategoryExtractor().getCategories


# DATABASE_URL = f"postgresql://postgres:Orikkel1991@localhost:5432/ProSpector_Dev"
# engine = create_engine(DATABASE_URL)
# categories_df = pd.DataFrame(categories)
# categories_df.to_sql('gulesider_categories', con = engine, if_exists='replace'),











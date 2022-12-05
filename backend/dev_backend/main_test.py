import time

start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import pandas as pd

''' Local Imports'''
# from SQL.config import Dev
# from backend.dev_backend.SQL.insert import Insert
# # from backend.dev_backend.SQL.query import Query, getAll1881, getAll1881Industries, getAllGulesiderIndustries, getAllGulesider, getAllProffIndustries, getAllGoogle, getAllProff, getAllBrregTable, getAllInputTable
# from extractors.industries_proff import IndustryProffExtractor
# from extractors.proff import ProffExtractor
# from extractors.industries_1881 import Industry1881Extractor
# from extractors._1881 import _1881Extractor
# from extractors.gulesider import GulesiderExtractor
# from extractors.industries_gulesider import IndustryGulesiderExtractor
# from extractors.google import GoogleExtractor
# from extractors.brreg import BrregExtractor
from SQL.query import Query

class Data:
    def __init__(self, query) -> None:
        self.query = query
        self.keys = self.getKeys()
        # self.data = self.getData()

    def getKeys(self) -> list:
        return [i for i in query[0].__dict__][1:]

    def getData(self) -> list:
        return [
            [   
                i.__dict__[  
                    [y for y in self.keys]
                ]   
            ] for i in query
        ]
        
    

query = Query('industry').get('Gulesider')#, 'first')
# lst = Data(query).getData()'
keys = Data(query).getKeys()
[y for y in keys]
# lst = [
#     [   i.__dict__['industries']   ] for i 
#     in query
# ]

# print(lst)     
# cols = [i for i in query[0].__dict__][1:]
# x = pd.DataFrame(lst, columns=[cols])
# print(x)
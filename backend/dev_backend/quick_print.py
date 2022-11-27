import time


from extractors._1881 import _1881Extractor; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 

from extractors.bransjer_proff import IndustryProffExtractor
from extractors.bransjer_1881 import Industry1881Extractor
from SQL.config import Dev#, DevSettings, Settings, engine, base
from SQL.query import getAll1881, getAll1881Industries, getAllCategories, getAllGulesider, getAllProffIndustries
from extractors.gulesider import GulesiderExtractor
from extractors.proff import ProffExtractor
from extractors.categories import CategoryExtractor

from SQL.insert import Insert



from SQL.query import getAllInputTable

print(pd.DataFrame(getAllInputTable()))
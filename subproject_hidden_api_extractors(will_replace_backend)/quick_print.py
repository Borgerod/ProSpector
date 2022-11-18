import time

import pandas as pd

from backend._1881 import _1881Extractor; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 

from backend.bransjer_proff import IndustryProffExtractor
from backend.bransjer_1881 import Industry1881Extractor
from SQL.config import Dev#, DevSettings, Settings, engine, base
from SQL.query import getAll1881, getAll1881Industries, getAllCategories, getAllGulesider, getAllProffIndustries
from backend.gulesider import GulesiderExtractor
from backend.proff import ProffExtractor
from backend.categories import CategoryExtractor

from SQL.insert import Insert

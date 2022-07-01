import requests
from bs4 import BeautifulSoup
import time
from fake_headers import Headers
import pandas as pd
import pprint


soup = BeautifulSoup(requests.get("https://www.gulesider.no/").content, "html.parser")
print(soup.prettify())
# doc = soup.get_all()

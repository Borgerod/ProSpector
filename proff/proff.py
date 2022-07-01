import requests
from bs4 import BeautifulSoup
import time
from fake_headers import Headers
import pandas as pd
import pprint


# industries = pd.read_csv('proff\industry_list.csv')
# print(industries)
f = open('proff\industry_list.txt', 'r')
content = f.read()
print(content)


# print("borgerød")
# print(industry_list)

# industries = []

# org_url = 'https://www.proff.no/bransjes%C3%B8k?q=Agenturhandel%20-%20annet'
# url = 'https://www.proff.no/bransjes%C3%B8k?q={ind}'
# soup = BeautifulSoup(requests.get(url).content, "html.parser")
# print(soup.prettify())
# # doc = soup.get_all()

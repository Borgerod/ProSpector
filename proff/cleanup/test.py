# # from time import sleep
# # from tqdm import tqdm
# # for i in tqdm(range(10)):
# #     sleep(3)


# # # from alive_progress import alive_bar; import time

# # # for total in 5000, 7000, 4000, 0:
# # #     with alive_bar(total) as bar:
# # #         for _ in range(5000): 
# # #             time.sleep(.001)
# # #             bar()


# # # for i in range(10):
# # #     with alive_bar(100, ctrl_c=False, title=f'Download {i}') as bar:
# # #         for i in range(100):
# # #             time.sleep(0.02)
# # #             bar()


# # # letters = [chr(ord('A') + x) for x in range(26)]
# # # with alive_bar(26, dual_line=True, title='Alphabet') as bar:
# # #     for c in letters:
# # #         bar.text = f'-> Teaching the letter: {c}, please wait...'
# # #         if c in 'HKWZ':
# # #             print(f'fail "{c}", retry later')
# # #         time.sleep(0.3)
# # #         bar()

# # def firstPage(url):
# #     df = pd.DataFrame(       index = [ 'bedrift',
# #                                         'avdeling',
# #                                         'telefon',
# #                                         'bransje',
# #                                         'org num', ] ).T
# #     soup = pullRequest(url)
# #     # content = soup.findAll('div', {'class':"search-container clear  low-priority"})
# #     # content = soup.findAll('div', {"class":"search-block-info"})
# #     # content = soup.findAll('div',{"class":"search-block-wrap"})
# #     content = soup.findAll('div', {"class":"search-block"})
# #     content = [i for i in content]
# #     with concurrent.futures.ThreadPoolExecutor() as executor:
# #         results = executor.map(firstPageWorker, content) 
# #         for data_list in results:
# #             row = pd.DataFrame(data_list, index = [ 'bedrift',
# #                                                     'avdeling',
# #                                                     'telefon',
# #                                                     'bransje',
# #                                                     'org num', ] ).T
# #             df = pd.concat([df, row], axis = 0)
# #     next_page_url = nextPageUrl(soup)
# #     df_firstPage = df.reset_index(drop = True)
# #     return df_firstPage, next_page_url

# # from concurrent.futures import ThreadPoolExecutor, as_completed
# # from tqdm import tqdm
# # import requests


# def download_file(url):
#     with requests.get(url, stream=True) as r:
#         for chunk in r.iter_content(chunk_size=50000):
#             pass
#     return url


# if __name__ == "__main__":
#     urls = ["http://mirrors.evowise.com/linuxmint/stable/20/linuxmint-20-xfce-64bit.iso",
#             "https://www.vmware.com/go/getworkstation-win",
#             "https://download.geany.org/geany-1.36_setup.exe"]

#     with tqdm(total=len(urls)) as pbar:
#         with ThreadPoolExecutor(max_workers=len(urls)) as ex:
#             futures = [ex.submit(download_file, url) for url in urls]
#             for future in as_completed(futures):
#                 result = future.result()
#                 pbar.update(1)


# from concurrent.futures import ThreadPoolExecutor, as_completed
# from tqdm import tqdm
# import requests
# import time
# import random


# def download_file(url, pbar):
#     for _ in range(30):
#         time.sleep(.50 * random.random())
#         pbar.update(1)
#     return url


# if __name__ == "__main__":
#     urls = ["http://mirrors.evowise.com/linuxmint/stable/20/linuxmint-20-xfce-64bit.iso",
#             "https://www.vmware.com/go/getworkstation-win",
#             "https://download.geany.org/geany-1.36_setup.exe"]

#     with tqdm(total=90) as pbar:
#         with ThreadPoolExecutor(max_workers=3) as ex:
#             futures = [ex.submit(download_file, url, pbar) for url in urls]
#             for future in as_completed(futures):
#                 result = future.result()



import time
start = time.perf_counter()
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import pandas as pd
import pprint
import re 
from industry_list import industries
import json
import concurrent.futures
BASE_URL = 'https://www.proff.no'



# progressbar test
from tqdm import tqdm




df = pd.DataFrame(       index = [ 'bedrift',
                                    'avdeling',
                                    'telefon',
                                    'bransje',
                                    'org num', ] ).T

# links = pd.read_csv('proff_data.csv', on_bad_lines = 'skip')
# # print(links)
# # links=links.to_numpy()
# print(links)
# print(type(links))

# df = df.dropna()
# df = df.reset_index()
df.to_csv('proff_data.csv')
print(df)

# import time
# start = time.perf_counter()
# import requests
# from bs4 import BeautifulSoup
# from fake_headers import Headers
# import pandas as pd
# import pprint
# import re 
# from industry_list import industries
# import json
# import concurrent.futures
# BASE_URL = 'https://www.proff.no'

# def pullRequest(url):
#     try:
#         r = requests.get(url, timeout=10)
#         soup = BeautifulSoup(r.content, "html.parser")
#        # soup = BeautifulSoup(requests.get(url,
#                          # timeout=10), "html.parser", features="lxml")
#                          # headers={'Cache-Control': 'nocache', 'Pragma': 'nocache'}))
#                          # headers = getHDR()))

#         r.raise_for_status()#, headers={'Cache-Control': 'nocache', 'Pragma': 'nocache'}).raise_for_status()
#     except (requests.exceptions.RequestException, ValueError) as e:
#         # print('Error caught!') 
#         # print(e)
#         print("="*91)
#         print("|                                              |")
#         print("|                WARNING: ERROR CAUGHT!                |")
#         print("|                                              |")
#         print("="*91)
#         print(f'                    {print(e)}')


#     return soup

# def nextUrlLoop(url):
#     soup = pullRequest(url)
#     next_urls = []
#     next_url = url
#     while next_url != "":
#         soup = pullRequest(next_url)
#         next_url = nextPageUrl(soup)
#         next_urls.append(next_url)
#     return next_urls



    

# def nextPageUrl(soup):
#     try:
#         a = soup.find('a',{'class': 'arrow ssproff-right'})
#         next_page_token = a['href']
#         next_page_url = BASE_URL + next_page_token
#     except TypeError:
#         next_page_url = ""
#     return next_page_url

# def genUrls(industries):
#     urls = []
#     for ind in industries:
#         url = f'https://www.proff.no/bransjes%C3%B8k?q={ind}'
#         urls.append(url)
#     return urls

# # MAIN TEST (MAP)
# industries = ['Adresseringsleverandører', 'Advokater og juridiske tjenester', 'Agenturhandel - annet','Akvakultur']
# def firstThreader():
#     index = 0
#     # result_list = []
#     urls = genUrls(industries)

#     # with concurrent.futures.ThreadPoolExecutor() as executor:
#     #     results = executor.map(pullRequest, urls)
#     #     soups = [soup for soup in results]
#         #   print() 
#     # next_urls=[]
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         results = executor.map(nextUrlLoop, urls)
#         for result in results:
#             print(result)
#             next_urls.append(result)
#     # print(next_urls)
#     # print(len(next_urls))
#     print(f"|                  Finished in {round(time.perf_counter() - start, 2)} second(s)                  |")
# firstThreader()

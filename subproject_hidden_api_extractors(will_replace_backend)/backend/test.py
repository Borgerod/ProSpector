import requests
from bs4 import BeautifulSoup
header = {
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
profile_url ="https://www.1881.no/kunstnerisk-virksomhet/kunstnerisk-virksomhet-vestland/kunstnerisk-virksomhet-bergen/a-borgeroed_106618216S0/?query=a+borger%c3%b8d"
profile_url_snippet = (profile_url.split("/")[6]).replace("_", "-")
url = f"https://www.regnskapstall.no/informasjon-om-{profile_url_snippet}"
response = requests.request("GET", url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
org_num = int(soup.find("th", string=" Org nr ").find_next().text.replace('\xa0', ''))
print(org_num)


# TEXT = '<br>test&nbsp;&nbsp;test'
# TEXT = TEXT.replace('<br>', '').replace('&nbsp;', '')
# print(TEXT)
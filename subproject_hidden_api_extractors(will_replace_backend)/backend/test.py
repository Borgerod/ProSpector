import requests
from bs4 import BeautifulSoup
import re 
class Test:
	def __init__(self) -> None:
		self.reached_limit = False
		self.base_url = "https://www.1881.no"
		self.industry = "advokat"
		self.company_name = None
		self.profile_url = None
		self.url = None

	def test(self):
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
		url ="https://www.1881.no/advokat"
		self.profile_url = "https://www.1881.no/adopsjon/adopsjon-vestfold-og-telemark/adopsjon-toensberg/adopsjonsforum_100352913S16/"
		
		profile_url_snippet = (self.profile_url.split("/")[-2]).replace("_", "-")
		print(profile_url_snippet)
		self.company_name = re.sub('[0-9]', '', profile_url_snippet).replace("-S", "")
		navn = self.company_name
		print(navn)

		# profile_name = soup.find("hl", class_="details-name")




		# response = requests.request("GET", url, headers = header)
		# soup = BeautifulSoup(response.content, "html.parser")
		# rows = soup.find_all("div", class_ = "box listing listing--business")
		# if not rows:
		# 	self.reached_limit = True
		# link_list = []
		# for row in rows:
		# 	# print(type(row))
		# 	a = row.find('a', href=re.compile(f'^/{self.industry}/'))
		# 	# a = row.find_all("a", href = True)  #TODO: see Current_issues [1]
		# 	# link_list = [i['href'] for i in a]
		# 	link_list.append(self.base_url + a['href'])
		# 	# print(link_list)
		# 	# print(a['href'])
		# 	# break
		# print(link_list)
			


if __name__ == '__main__':
	Test().test()


# eksempel profil url
'''
https://www.1881.no/adopsjon/adopsjon-vestfold-og-telemark/adopsjon-toensberg/adopsjonsforum_100352913S16/
https://www.1881.no/adopsjon/adopsjon-nordland/adopsjon-bodoe/adopsjonsforum_100352913S3/
https://www.1881.no/adopsjon/adopsjon-vestland/adopsjon-bergen/adopsjonsforum_100352913S11/
https://www.1881.no/adopsjon/adopsjon-rogaland/adopsjon-sandnes/adopsjonsforum_100352913S12/
https://www.1881.no/adopsjon/adopsjon-troendelag/adopsjon-verdal/adopsjonsforum_100352913S6/
https://www.1881.no/adopsjon/adopsjon-moere-og-romsdal/adopsjon-aalesund/adopsjonsforum_100352913S10/
https://www.1881.no/adopsjon/adopsjon-nordland/adopsjon-mo-i-rana/adopsjonsforum_100352913S5/
https://www.1881.no/adopsjon/adopsjon-agder/adopsjon-lillesand/adopsjonsforum_100352913S13/
https://www.1881.no/adopsjon/adopsjon-viken/adopsjon-sarpsborg/adopsjonsforum_100352913S17/
https://www.1881.no/adopsjon/adopsjon-nordland/adopsjon-sortland/adopsjonsforum_100352913S4/
https://www.1881.no/adopsjon/adopsjon-troendelag/adopsjon-trondheim/adopsjonsforum_100352913S7/
https://www.1881.no/adopsjon/adopsjon-vestland/adopsjon-foerde/adopsjonsforum_100352913S9/
https://www.1881.no/adopsjon/adopsjon-moere-og-romsdal/adopsjon-molde/adopsjonsforum_100352913S8/
https://www.1881.no/adopsjon/adopsjon-troms-og-finnmark/adopsjon-tromsoe/adopsjonsforum_100352913S2/
https://www.1881.no/adopsjon/adopsjon-oslo/adopsjon-solli/adopsjonsforum_100352913S1/
https://www.1881.no/adopsjon/adopsjon-innlandet/adopsjon-hamar/adopsjonsforum_100352913S15/
https://www.1881.no/adopsjon/adopsjon-vestfold-og-telemark/adopsjon-porsgrunn/adopsjonsforum_100352913S14/
https://www.1881.no/adopsjon/adopsjon-innlandet/adopsjon-kapp/danielsen-tak-og-bygg-v-tommy-danielsen_101394646S1/
https://www.1881.no/adopsjon/adopsjon-rogaland/adopsjon-stavanger/hinna-auto-nilsen_106938558S1/
https://www.1881.no/adopsjon/adopsjon-agder/adopsjon-kristiansand-s/inor-adopt_100347174S1/
'''
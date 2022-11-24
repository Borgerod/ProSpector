	# def setProfileLink(self, row):
	# 	h2 = row.find('h2', class_="listing-name")
	# 	# a = row.find('a', href = re.compile(f'^/{self.industry}/'))
	# 	a = h2.find('a')
	# 	# if a is None:
	# 	# 	a = row.find('a', href = re.compile(f'^/tlf/'))
	# 	self.profile_url = self.base_url + a['href']	
    
    # def checkForPayedEnrtryInProfile(self, profile:BeautifulSoup) -> bool:
	# 	# if 'Andre søker også' not in profile.text:
	# 	# 	print(f"TRUE (found no Andre søker også) : {self.profile_url}")
	# 	# 	return True
	# 	if 'Søkeord' in profile.text:
	# 		print(f"TRUE (found Søkeord) : {self.profile_url}")
	# 		return True
	# 	else:
	# 		print("FALSE")
	# 		return False

	# def something(self, profile):
	# 	if self.checkForPayedEnrtryInProfile(profile) == True:
	# 		self.getAndInsertCompanyInfoToDb()



	# def getOrgnum(self, soup):
	# 	''' gets org_num from regnskapstall.no 
	# 	'''	
	# 	try:
	# 		return 
	# 	except AttributeError:
	# 		print(self.profile_url)
	
	# def getCompanyName(self, soup):
	# 	''' gets company_name & org_num from regnskapstall.no, since we already getting org_num from there. 
	# 		++ then we get the full legal name of the company, sometimes 1881 name is wrong, e.g."1 default"
	# 	'''
	# 	return soup.find("th", string = " Juridisk selskapsnavn ").find_next().text#.replace('\xa0', '')


	
	# def OLDgetCompanyName(self): #! NOT IN USE 
	# 	# try:
	# 	return re.sub('[0-9]', '', self.profile_url_snippet).replace("-S", "").replace("-", " ")
	


# '''
# verification barrier:
#    local_storage = { 
#         "_grecaptcha" : "09ADzA0mBJ-EOfULZqqrJeXR-qrhZ4CHuiBujAqajdfL5zQeDVz7xGWn01cirjRlE7KGaTMczlOvRpBYDks0FaQwmqkCscg23Tw00"
#     }


    # good_coockies = {
    #     "PSIDCC":"AIKkIs3htvJKkqghl4YwJI83s79YSp8pT4sWiyglevpDIVkHUDNtKF2n6slaYMB1pbxyWf4YaWGg",
    #     "SID":"QQhZfCEBuIc1GJIsfVudeOS-qSSeRiWI6fAGj6hrZPEFI3PE6gb0NGNEu69oSdcqWum-bw.",
    #     "SAPISID":"QgJl6godncPVtK_x",
    #     "HSID":"Aya3xpJ7y9oLuYjQM",
    #     "__Secure-3PSIDCC":"AIKkIs3nSOPvfqgCD9jgKIESkPFnLZD40QNG4hmUrG3jCOqVV52b-xD7HWDeGoEubrlZNH6A1vgg",
    #     "APISID":"eoWNVoajHbvXDAFK/A-CI7Oz4yOjAKGRrE",
    #     "SAPISID":"QgJl6godncPVtK_x",
    #     "APISID":"eoWNVoajHbvXDAFK/A-CI7Oz4yOjAKGRrE",
    #     "HSID":"A3vphuCAXek80i7XW",
    #     "__Secure-3PSID":"QQhZfBww80R6L2LQPUb4AkuKlmlR1tmYIA9d-4Xx8CViIlcx6hCnIHNFcOFZ4jxj71Ba3w.",
    #     "SID":"QQhZfBww80R6L2LQPUb4AkuKlmlR1tmYIA9d-4Xx8CViIlcxVIgbR1sVni5dVKs-ELa7Eg.",
    #     "__Secure-3PSID":"QQhZfCEBuIc1GJIsfVudeOS-qSSeRiWI6fAGj6hrZPEFI3PE36eP_uQUUxkL2I5NQNOUUg.",
    #     "__Secure-1PSID":"QQhZfCEBuIc1GJIsfVudeOS-qSSeRiWI6fAGj6hrZPEFI3PENTMqzX6VsV3NRdrO96MtCw.",
    #     "SIDCC":"AIKkIs3Q27Yl9vo5AtaTWYSp9h0UVAgKlF18flwnPXtmPiWybTpRKzv3y9p5NR1FSk3KSvrnZSFS",
    #     "SSID":"AnE6mOCTmBxPmP-Ag",
    #     "__Secure-3PAPISID":"QgJl6godncPVtK_x",
    #     "NID":"511=PLFZYSx7NsT_0XQ_oXp2b_fcvBBLta1_We6Wo2IgIT3ORj-q0KZrEo5OcjC2xwyLLTm8WWDNavidDQn5ZpX4mA_0mmh02L2p9bZF12PQ-wypPCwUGsH5vOfm6ZxXp9KzGrl43IR7aMcWeuj0eLwX64NamVHBmfj7ayUSJwWqeb5jtDl2XEJ2UHaBKL6q16u9SYkXAP4wR9WciY686ytPoci2h1yu4d-Oynxa-yealwnCfSbWk7jCxwZo0sCa5ZNjfZtYykHU3CbXIsKuWST6Xu5qsd3Pccij0_zlBA3Rw1l1evluH0utMgRU33tmGthTthL9_jGRP_2As1KY8cZKB16HUONOIjsT9_mU9Jk9GNf_U_am0styLWczBX5hM176XRnlCGkBfC5T-KYXwF1uYvhh9z2tKgh0y6xKsKYzY2jGjAGyc5Z0vWmQxoW2hgh1DyMY2j4eNbEewIW-qr6rWzQJ",
    #     "1P_JAR":"2022-11-09-16",
    #     "ANID":"AHWqTUkBZUErv3xVPCgKmN_H7ksO-Z_HqMg6DTx9zmjt1LvaKZQn6CwSF76XzH3J",
    #     "CONSENT":"YES+srp.gws-20210519-0-RC1.no+FX+871",
    #     "NID":"511=TwKiS_ktgeBwFwpY0GRFAZhjtVEqZqUAEif3Xg3rashc_olNOYO1qLrO4KXI60CGBnJ28GRjceprmT0GbbHUQTmcWPEhnBX5GeJFopY0u_Ih0dda8kxRmH0YiViR4ZvFp6t5I1O2Kdnyighz3dFG1lsB2vkwoAltaGDhvvlC8xkFtBKXrTeeKb70U14l4D-q1kHfNPxoW-UGeQxduBQC1OB_WSoZee_loNKCo7JbzzPY2gW_CgV8p45j6x0clU6wV-cnqMNzQx0hc31F1jOfh3B8yNQ2lw",
    #     "AEC":"AakniGOZ_F9bgvDjwCGYWfU5eVlxyPStvdnK6Y5iiruJSheD2c7PaM-K6Xg=",
    #     "ASP.NET_SessionId":"du51yujdlhfvf5ag1xdgeida",
    #     "CONSENT":"YES+srp.gws-20210519-0-RC1.no+FX+566",
    #     "__uzmdj2":"1668014054",
    #     "_gat_UA":"-28557615-13",
    #     "__uzmcj2":"120509116625",
    #     "__uzmc":"2389910358329",
    #     "__uzmd":"1668013538",
    #     "_ga_J63ZNLRLL4":"GS1.1.1668013534.2.1.1668014054.60.0.0",
    #     "__mbl":"%7B%22u%22%3A%5B%7B%22uid%22%3A%22hqgB1zLiXNbiQuKK%22%2C%22ts%22%3A1668014054%7D%2C1668104054%5D%7D",
    #     "_ga":"GA1.1.1596546858.1668009105",
    #     "captchaResponse":"1",
    #     "_ga_60EFTS75DG":"GS1.1.1668013534.2.1.1668014054.60.0.0",
    #     "__uzmb":"1666783142",
    #     "__uzmaj2":"4020e8d3-c6c5-4c2f-acd4-97eb3cd5e853",
    #     "__uzma":"50cc4c09-cad5-4619-b323-6e6f87171b5a",
    #     "__ssds":"2",
    #     "__uzmbj2":"1668009105",
    #     "_gid":"GA1.2.1354368843.1668009105",
    #     "__ssuzjsr2":"a9be0cd8e"
    # }



# https://www.1881.no/adopsjon/
# https://www.1881.no/Adopsjon/
# import requests
# response = requests.request("GET", 'https://www.1881.no/Adopsjon/', headers={
#                 "cookie": "__uzma=e69d520f-a8db-46ec-b5d1-7d2e26930e28; __uzmc=163051371814; __uzmb=1668010547; __uzmd=1668010570;captchaResponse=1; Expires=null; Path=/; Domain=www.1881.no",
#                 "authority": "cdn.pbstck.com",
#                 "accept": "*/*",
#                 "accept-language": "en-US,en;q=0.9",
#                 "cache-control": "no-cache",
#                 "origin": "https://www.1881.no",
#                 "pragma": "no-cache",
#                 "sec-ch-ua": "^\^Google",
#                 "sec-ch-ua-mobile": "?0",
#                 "sec-ch-ua-platform": "^\^Windows^^",
#                 "sec-fetch-dest": "empty",
#                 "sec-fetch-mode": "cors",
#                 "sec-fetch-site": "cross-site",
#                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
#             })
# print(response.text)
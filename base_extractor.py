
'''
	* from base_extractor import genSearchTerm, linkBuilder, pullRequest
'''
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers



def genSearchTerm(term):
	'''
		build a search phrase based on company name
	'''
	return term.replace(' ', '+') #* -> url 

def pullRequest(url, source, org_num, search_term):
	'''
		1. makes a pull request from gulesider.no.
		2. then checks the connection.
		3. then returns a soup.
		4. If a bad request occours; then it will save the error to "gulesider_error_table"
	'''
	r = requests.get(url, timeout = 10)
	r.raise_for_status() #? a bit unsure why i have this here
	return BeautifulSoup(r.content, "html.parser") #* -> soup
	
	# * [ikke fjern koden under]
		# try:
		# 	r = requests.get(url, timeout = 10)
		# 	soup = BeautifulSoup(r.content, "html.parser")
		# 	r.raise_for_status()

		
		# except (requests.exceptions.RequestException, ValueError) as e:
		# 	''' 
		# 	if exception occurred:
		# 		- prints error & related url
		# 		- sends the faulty url (++) to errorSave() from error_save.py for later use
		# 		- returns an empty soup
		# 	'''	
		# 	print("="*91)
		# 	print("|											  |")
		# 	print("|				WARNING: ERROR CAUGHT! 				  |")
		# 	print("|											  |")
		# 	print("="*91)
		# 	print(f'					{print(e)}')
		# 	errorManager(org_num, search_term, url, e)
		# 	# errer_df = pd.DataFrame([org_num, search_term, url, e], columns = ['org_num', 'search_term', 'url', 'error_message'])
		# 	# errorSave(url, e, source) #Currently not in nuse (not yet finished)
		# 	# soup = ""
			# pass 
		# return soup

def getRequest(url, org_num, search_term):
	'''
		1. makes a pull request from gulesider.no.
		2. then checks the connection.
		3. then returns a soup.
		4. If a bad request occours; then it will save the error to "gulesider_error_table"
	'''
	return requests.get(url, timeout = 10) #* -> req 

def getSoup(req):
	return BeautifulSoup(r.content, "html.parser") #* -> soup
	




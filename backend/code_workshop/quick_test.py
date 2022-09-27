import re 

class Extration:
	def __init__(self):
		self.search_term = 'BAUNEN FISK OG VILT AS maps'
		self.verify = None
		self.alt_verify = None
		self.alt_search_term = None
		# __________________________
		self.is_reqistered = False
	
	def start(self):
		self.setVerify()
		self.setAltVerify()
		self.setAltSearchTerms()
		self.checkRegistered()

	def setVerify(self):
		self.verify = 'Baunen fisk og Vilt AS maps'

	def setAltVerify(self):
		self.alt_verify = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in self.verify.split("\n")][0]
	
	def setAltSearchTerms(self):
		for ch in [' AS',' ASA', ' AB']:
			if ch in self.search_term:
				self.alt_search_term = self.search_term.replace(ch,"")

	def getLowerCaseList(self):
		return [
				list(map(str.lower, [self.verify, self.alt_verify])), 
				list(map(str.lower, [self.search_term, self.alt_search_term]))
				]

	def checkRegistered(self):
		self.is_reqistered = (True if any(x in self.getLowerCaseList()[0] for x in self.getLowerCaseList()[1]) else False)

	@property
	def result(self):
		return self.is_reqistered

	# def checkRegistered(self):
		# verifications = list(map(str.lower, [self.verify, self.alt_verify]))
		# search_terms = list(map(str.lower, [self.search_term, self.alt_search_term]))
		# return any(x in  list(map(str.lower, [self.verify, self.alt_verify])) 
		# 			for x in list(map(str.lower, [self.search_term, self.alt_search_term])))

		
		# self.is_reqistered = (True if self.checkRegistered() else False)
		
		# if any(x in verifications for x in search_terms):
		# 	self.is_reqistered = True
		# else:
		# 	self.is_reqistered = 'Usikkert'

E = Extration()
E.start()
print(E.result)
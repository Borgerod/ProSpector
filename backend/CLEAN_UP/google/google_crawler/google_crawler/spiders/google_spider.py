import scrapy 
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class firstSpider(scrapy.Spider): 
	name = "basic"

	start_urls = [ 
		"https://www.google.com/search?q=journal+dev"
	 ]

	def linkBuilder():
		base_url = 'https://www.google.com/search?q='


	def parse(self, response):
			xlink = LinkExtractor()
			for link in xlink.extract_links(response):
				print(link)

	def parse(self, response):
		xlink = LinkExtractor()
		for link in xlink.extract_links(response):
			if len(str(link))>200 or 'Journal' in link.text:
				print(len(str(link)),link.text,link,"\n")


# //*[@id="rhs"]/div
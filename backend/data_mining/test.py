from config import payload, tablenames, settings
from postgres import *
import numpy as np
from tabulate import tabulate
import pandas as pd

# pd.options.display.max_rows = None				# Rows 	   (length)
pd.options.display.max_columns = 4				# Columns  (width)
pd.options.display.max_colwidth = 20			# Columns  (column display border)
pd.options.display.width = 2000					# Whole	   (dataframe display border)


class Data:

	def __init__(self):
		self.tablename = None

	def getBrregTable(self):
		return fetchData('brreg_table', to_user_api = False).drop('index', axis=1)
		
	def getGoogleTable(self):
		return fetchData('google_input_table', to_user_api = False)

	def subtractGoogleFromBrreg(self):
		brreg = self.getBrregTable().set_index(['org_num'])
		google = self.getGoogleTable().set_index(['org_num'])
		no_ads = (pd.concat([google, brreg], axis = 0)).drop_duplicates()
		has_ads = brreg[brreg.index.isin(google.index)]
		
		print(has_ads.iloc[2])



class Input:
	def getTablenames(self):
		return ['brreg_table', 'google_input_table']


def main():
	i = Input()
	d = Data()
	df = d.subtractGoogleFromBrreg()

if __name__ == '__main__':
	main()

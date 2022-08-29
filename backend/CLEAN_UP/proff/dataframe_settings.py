import pandas as pd

def dataframeSettings(settings):
	'''
	decides the settings for pandas dataframes;
		0 = settings: default 
		1 = settings: dataframes print full width
		2 = settings: dataframes print full width & length 
	'''
	if settings == 1:
		pd.set_option('display.max_colwidth', None)		# Columns  (width)
		pd.set_option('display.max_columns', None)		# column display border
		pd.set_option('display.width', None)			# dataframe display width
	
	elif settings == 2:
		pd.set_option('display.max_row', None)			# Rows  (width)
		pd.set_option('display.max_columns', None)
		pd.set_option('display.max_colwidth', None)		
		pd.set_option('display.width', None)

	else: 
		pass
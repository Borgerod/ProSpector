import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
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


def testPrint():
	df = pd.read_csv('../_output_data/proff_data.csv')
	print(df)
	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")


if __name__ == '__main__':
	testPrint()
	

# def testPrint(settings):
# 	dataframeSettings(settings)
# 	df = pd.read_csv('../_output_data/proff_data.csv')
# 	print(df)
# 	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")


# if __name__ == '__main__':
# 	testPrint(settings)
	

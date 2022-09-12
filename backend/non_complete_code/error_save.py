import pandas as pd
 
'''
	# ! NB: OLD CODE, not yet updated for database usage
'''


def errorSave(url, e, error_source):

	'''
	this function is triggered whenever an exception has occurred from pullRequest().

	saves url (+error message and error source) in a csv file, so it can be scraped or analysed later. 
	Then we can re-scrape just the faulty links and don't have to 
	scrape everything to complete the dataset.

	Note: 
		The function will also check the source of the error, [guleside.py, proff_data.py, proff_links.py, etc]
		and either: (currently not decided)
		- Option 1: tag the row with the source (third column), df does require parsing if its going to be used
		- Option 2: create seperate csv files based on the sources, e.g.: 'faulty_links_guleisder.csv'
	'''
	

	'''	Option 1: 
			Tag the row with the source (third column) '''
	file_name = faulty_links


	'''	Option 2: 
			Create seperate DFs based on source-tag '''
	if error_source == 'gulesider.py':
		file_name =  'faulty_links_gulesider'
	elif error_source == 'proff_data.py':
		file_name = 'faulty_links_proff_data'
	elif error_source == 'proff_links.py':
		file_name = 'faulty_links_proff_links'
	elif error_source == 'google.py':						#PLACEHOLDER, not yet created 
		file_name = 'faulty_links_google'					#PLACEHOLDER, not yet created 


	''' Creates update (dataframe) from input & Makes the path '''
	update =  pd.DataFrame([url, e, error_source], columns = ['url', 'error message', 'error source'])	
	path = f'../_output_data/{file_name}.csv'	
	

	'''Checks if file exists then gets or creates it'''
	if file.exists ():
		faulty_links = pd.read_csv(path)
	else: 
		faulty_links = pd.DataFrame(columns = ['url', 'error message'])


	''' Concat then saves the data in path '''
	faulty_links_updated = pd.concat([faulty_links, update], axis = 0)
	faulty_links_updated = faulty_links_updated.reset_index()
	faulty_links_updated = faulty_links_updated.to_csv(path, index = False)

if __name__ == '__main__':
	errorSave()

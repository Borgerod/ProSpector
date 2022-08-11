''' ____ Local imports _______ '''
from proff_del1 import proffLinkDownloader
from proff_del2 import proffDataDownloader
from data_cleaner import checker
from settings_test import dataframeSettings


'''
____ proff main function ___________

Oppgave: kjøre py filene i denne folderen

'''

def proffMain():
	dataframeSettings(settings = 1) # decide print settings for pandas; see dataframe_settings.py
	proffLinkDownloader()			# download links from all the pages, creates dataframe; links.csv
	proffDataDownloader()			# download data from all the links, creates dataframe; proff_data.csv
	dataCleaner()					# checks, edits and cleans data; proff_data.csv
	''' 
	PS: dataCleaner is currently not in use (unfinished), 
	now it only prints df w/ some temp edits 
	'''
	
if __name__ == '__main__':
	proffMain()

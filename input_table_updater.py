'''
	this code will make sure to keep input_list up to date, by doing two things: 

	1. whenever google.py and gulesider.py has sucsessfull extracted information about a company; 
	this code will then remove that company from input list.


	2. whenever brreg.py has made changes to brreg_table, that company will be added back to input list so gulesider.py and google.py can re-scrape them. 
'''
# # local imoprts 
# from config import payload, tablenames, settings
# from postgres import databaseManager, cleanUp, fetchData, checkForTable, postLastUpdate, deleteData
# # from file_manager import *

# def checkGoogleTable(org_num):
# 	'''
# 		if google table contains data on org_num; 
# 			return 1
# 		else:
# 			return 0 
# 	'''
# 	google_table = fetchData(tablename='google_table')
# 	google_table.set_index(org_num)
# 	if google_table[org_num]:
# 		return 1
# 	else:
# 		return 2


# def brregUpdateValidator()
# 	brreg_update_status = fetchData(tablename='google_table')



# # ! USIKKER PÅ OM JEG VIL GJØRE DET PÅ DENNE MÅTEN...

import pandas as pd 
import numpy as np
import pandas as pd 
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
import concurrent.futures
from inspect import currentframe, getframeinfo


# ___ local imports ________
from config import payload, tablenames, settings
# from postgres import databaseManager, cleanUp, fetchData, checkForTable, postLastUpdate, deleteData ,insertData
from file_manager import *
from postgres import *
'''
	this is the algorythm that decides what is going to output or not.
'''
def test_function():
	# brreg = fetchData(tablename = 'input_table')
	gulesider =  fetchData(tablename = 'gulesider_table')
	google = fetchData(tablename = 'google_table')
	gulesider.org_num = gulesider.org_num.astype(int).astype(str)

	# gulesider.set_index(['org_num'],  inplace = True)
	# google.set_index(['org_num'],  inplace = True)


	# brreg = fetchData(tablename = 'brreg_table')
	# print((brreg.loc[brreg['org_num'] == 912992950]).T)
	# brreg = brreg.loc[brreg['org_num'] == 912992950]
	# print(brreg.columns)
	# print(brreg.values)


	''' find what gulesider and google have in common'''
	common1 = gulesider.merge(google, on = ['org_num'])
	# print(common1)


	#* SNIPPETS FOR EASIER TESTING 
	gulesider = (gulesider.loc[gulesider['org_num'] == '912992950'])
	google = (google.loc[google['org_num'] == '912992950'])
	# brreg = pd.DataFrame([[	'912992950',
							# '1. LØRENSKOG 3 SPEIDERGRUPPE',
							# '2009-02-16',
							# 0,
							# False,
							# False,
							# True,
							# False,
							# False,
							# False,
							# 'Bokmål',
							# '1985-06-03',
							# 'NaN',
							# 'www.1lorenskog3.no',]],columns = ['org_num',
							# 'navn',
							# 'registreringsdato',
							# 'antall_ansatte',
							# 'foretaks_registeret',
							# 'stiftelses_registeret ',
							# 'frivillighets_registeret ',
							# 'konkurs',
							# 'under_avvikling',
							# 'under_tvangsavvikling_eller_oppløsning',
							# 'maalform',
							# 'stiftelsesdato',
							# 'siste_innsendt_årsregnskap',
							# 'hjemmeside',])
	brreg = pd.DataFrame([['912992950', '1.ST.GEORGS GILDE I MOLDE' ,'2013-12-21', 0 ,False ,False, False,
						  False, False, False ,'Bokmål', '1962-05-11', 'NaN', None]],
						columns = ['org_num', 'navn', 'registreringsdato', 'antall_ansatte',
							       'foretaks_registeret', 'stiftelses_registeret',
							       'frivillighets_registeret', 'konkurs', 'under_avvikling',
							       'under_tvangsavvikling_eller_oppløsning', 'maalform', 'stiftelsesdato',
							       'siste_innsendt_årsregnskap', 'hjemmeside']	)
	# print(len(gulesider.columns))
	# print(len(google.columns))
	# print(len(brreg.columns))

	gulesider = gulesider.reset_index(drop = True)
	google = google.reset_index(drop = True)
	brreg = brreg.reset_index(drop = True)


	# gulesider, google, brreg,
	df = pd.concat([gulesider,google,brreg], axis = 1)
	df = df.loc[:,~df.columns.duplicated()].copy()

	score = 0
	for i in df.iloc[0]:
		if i == False:
			score += 1
	# print(score)
	# print(df.T)

	# df = df[['org_num', 'navn']]
	# print(df)


'''
	REFERANCE, example
		                                           47
		org_num                              893747052
		navn              1. Lørenskog 3 Speidergruppe
		tlf                                       None
		daglig_leder               Jon Øyvind Nordberg
		styreleder                 Jon Øyvind Nordberg
		er_Eierbekreftet                         False
		har_Beskrivelse                          False
		har_Fritekst                             False
		har_Dyplenker                            False
		har_SEO                                  False
		har_Premium_SEO                          False
		har_Åpningstider                         False
		har_Facebook                             False
		facebook                                  None


		                                              3
		org_num                               893747052
		navn               1. LØRENSKOG 3 SPEIDERGRUPPE
		google registrert                         False
		google erklært                            False


		                                                             100                           1078759
		org_num                                                    893747052                     893747052
		navn                                    1. LØRENSKOG 3 SPEIDERGRUPPE  1. LØRENSKOG 3 SPEIDERGRUPPE
		registreringsdato                                         2009-02-16                    2009-02-16
		antall_ansatte                                                     0                             0
		foretaks_registeret                                            False                         False
		stiftelses_registeret                                          False                         False
		frivillighets_registeret                                        True                          True
		konkurs                                                        False                         False
		under_avvikling                                                False                         False
		under_tvangsavvikling_eller_oppløsning                         False                         False
		maalform                                                      Bokmål                        Bokmål
		stiftelsesdato                                            1985-06-03                    1985-06-03
		siste_innsendt_årsregnskap                                       NaN                           NaN
		hjemmeside                                        www.1lorenskog3.no            www.1lorenskog3.no
'''


'''
	FURTHER REFERANCE, example
		16
		                                                                0
		org_num                                                 912992950
		navn                                    1.St.Georgs Gilde i Molde
		tlf                                                          None
		daglig_leder                                           Elin Asker
		styreleder                               Ingar Lauritz Fladby Aas
		er_Eierbekreftet                                            False
		har_Beskrivelse                                             False
		har_Fritekst                                                False
		har_Dyplenker                                               False
		har_SEO                                                     False
		har_Premium_SEO                                             False
		har_Åpningstider                                            False
		har_Facebook                                                False
		facebook                                                     None
		google registrert                                            True
		google erklært                                              False
		registreringsdato                                      2013-12-21
		antall_ansatte                                                  0
		foretaks_registeret                                         False
		stiftelses_registeret                                       False
		frivillighets_registeret                                    False
		konkurs                                                     False
		under_avvikling                                             False
		under_tvangsavvikling_eller_oppløsning                      False
		maalform                                                   Bokmål
		stiftelsesdato                                         1962-05-11
		siste_innsendt_årsregnskap                                    NaN
		hjemmeside                                                   None

		Index(['org_num', 'navn', 'tlf', 'daglig_leder', 'styreleder',
		       'er_Eierbekreftet', 'har_Beskrivelse', 'har_Fritekst', 'har_Dyplenker',
		       'har_SEO', 'har_Premium_SEO', 'har_Åpningstider', 'har_Facebook',
		       'facebook', 'google registrert', 'google erklært', 'registreringsdato',
		       'antall_ansatte', 'foretaks_registeret', 'stiftelses_registeret',
		       'frivillighets_registeret', 'konkurs', 'under_avvikling',
		       'under_tvangsavvikling_eller_oppløsning', 'maalform', 'stiftelsesdato',
		       'siste_innsendt_årsregnskap', 'hjemmeside'],
		      dtype='object')
'''


def mergeOutputTables():
	'''
		takes output tables from the extractors and creates a merged output_table (input table for google.py)
	'''
	# parseTablenames(file_name, **kwargs)
	tablenames = [
	'gulesider_output_table',
	'I88I_output_table',
	'proff_output_table',]
	output_table = pd.DataFrame(columns = ['org_num', 'navn'])
	for tablename in tablenames:  
		df = fetchData(tablename)
		output_table = concatData(output_table, df)
	insertData(output_table, tablename = 'google_input_table')

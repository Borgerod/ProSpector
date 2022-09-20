from postgres import *
import pandas as pd

def createOverview(client_org = 'Mediavest'):
	chunk_size = 40
	tablename = 'call_list'
	df = fetchData(tablename, to_user_api=True)

	chunks = []
	num_chunks = len(df) // chunk_size + 1
	for i in range(num_chunks):
		chunks.append(df[i*chunk_size:(i+1)*chunk_size])

	list_ids = list(range(0,len(chunks)))
	overview = []
	for i in list_ids:
		kunde_id = None
		er_ledig = True
		er_ferdig = False
		list_start = i*40
		list_limit = (i+1)*40
		list_cols = [i, 
					list_start,
					list_limit,
					kunde_id,
					er_ledig,
					er_ferdig,
					]
		overview.append(list_cols)
	overview = pd.DataFrame( overview,
		columns = ['liste_id','liste_start',
				   'liste_limit', 
				   'kunde_id', 'er_ledig','er_ferdig',
				   # 'org_num_liste'
				   ],)
	tablename = f'call_list_overview_{client_org}'
	# print(overview)
	databaseManager(overview, tablename, to_user_api=True)
createOverview(client_org = 'mediavest')




def markCallListWithListID(client_org = 'Mediavest'):
	chunk_size = 40
	tablename = 'call_list'
	df = fetchData(tablename, to_user_api=True)

	chunks = []
	num_chunks = len(df) // chunk_size + 1
	for i in range(num_chunks):
		chunks.append(df[i*chunk_size:(i+1)*chunk_size])
	
	list_ids = list(range(0,len(chunks)))
	
	list_id_col = []
	for i in list_ids:
		for y in range(0, chunk_size):
			list_id_col.append(i)
			
	list_id_col = list_id_col[:len(df.index)]
	df['liste_id'] = list_id_col
	# databaseManager(df, tablename, to_user_api=True)
# markCallListWithListID(client_org = 'Mediavest')
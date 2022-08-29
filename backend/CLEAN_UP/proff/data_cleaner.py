import pandas as pd
from industry_list import industries
import concurrent.futures

def dataCleaner():
	df = pd.read_csv('../_output_data/proff_data.csv')
	df = df.drop_duplicates(subset = ['org num'], keep = 'first')

	# df = df['avdeling']
	# df = df.sort_values('bedrift')
	# print(df)

	# print(df.loc[df['bedrift'].isin(['&'])])
	df = df[df['bedrift'].str.contains("&")]
	df = df.reset_index(drop=True)
	print(df)

# if __name__ == '__main__':
	# dataCleaner()


def genUrls(ind):
	# urls = []
	# for ind in industries:
	url = f'https://www.proff.no/bransjes%C3%B8k?q={ind}'
	# urls.append(url)
	return url



def dataCleaner():
	links = pd.read_csv('../_input_data/links.csv')
	base_links = pd.read_csv('../_input_data/base_links.csv')
	links.drop_duplicates()
	links = links.reset_index(drop=True)
	print(links)
	new_links = pd.concat([links, base_links], axis=0)
	new_links = new_links.reset_index(drop=True)
	new_links = new_links.dropna()
	new_links = new_links.drop_duplicates(subset=['links'], keep=False)
	new_links = new_links.reset_index(drop=True)
	new_links.to_csv('../_input_data/links.csv', index = False)
	# print(new_links)
	# print(new_links)
	# print(new_links)
	# print()
	# print()
	# print(len(links))
	# print(len(new_links))




	# duplicates = pd.merge(links, base_links, how='inner',
 #                  left_on=['links'], right_on=['base_links'],
 #                  left_index=True)
	# USERS = pd.merge(USERS, EXCLUDE, on=["email", "name"], how="outer", indicator=True)

	# # drop the indices from USERS
	# USERS = USERS.drop(duplicates.index)
	# print(len(links))
dataCleaner()
# resultlist=[]
# with concurrent.futures.ThreadPoolExecutor() as executor:
# 	results = executor.map(genUrls, industries)
# 	for result in results:
# 		resultlist.append(result)
# # df = pd.DataFrame(resultlist)
# df.to_csv('../_input_data/links.csv', index = False)


# df = pd.read_csv('../_output_data/proff_data.csv')
# df = df.drop_duplicates(subset = ['org num'], keep = 'first')

# # df = df['avdeling']
# # df = df.sort_values('bedrift')
# # print(df)

# # print(df.loc[df['bedrift'].isin(['&'])])
# df = df[df['bedrift'].str.contains("&")]
# df = df.reset_index(drop=True)
# print(df)
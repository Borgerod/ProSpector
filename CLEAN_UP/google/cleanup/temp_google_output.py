import pandas as pd
import numpy as np
# pd.set_option('display.max_row', None)      # Rows     (length)
pd.set_option('display.max_columns', None)    # Columns  (width)
pd.set_option('display.max_colwidth', 20)   # Columns  (column display border)
pd.set_option('display.width', 2000)      # Whole    (dataframe display border)


df_old = pd.read_csv('../_output_data/google_maps_data.csv')
print(df_old)

# input_df = pd.read_csv('../_output_data/gulesider_data.csv')
# input_df = input_df[['bedrift', 'org num']][:15]
# print(input_df)
# df_old = pd.read_csv('../_output_data/gulesider_data.csv')
# print(df_old.head())


# df_old = pd.read_csv('../_output_data/proff_data.csv')
# print(df_old.head())





# companies = np.array((y,x for y,x in zip(input_df['bedrift'], input_df['org num'])), dtype=str)
# companies = np.array((input_df['bedrift'], input_df['org num']), dtype=str)
# print(companies[0])
# org_num = inputs['org num']
# input_list = 

import pandas as pd
import os


data_path = 'data/'
files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
dfs = [pd.read_csv(os.path.join(data_path, file)) for file in files]
combined_df = pd.concat(dfs, ignore_index=True)

pink_df = combined_df[combined_df['product'] == 'pink morsel'].copy()

pink_df['price'] = pink_df['price'].replace('[\$,]', '', regex=True).astype(float)

pink_df['sales'] = pink_df['price'] * pink_df['quantity']

final_df = pink_df[['sales', 'date', 'region']]

final_df.to_csv('pink_morsel_sales.csv', index=False)

#this file combines all csv data files into one 
import pandas as pd

csv_files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']

df_list = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

# Save the output
combined_df.to_csv('combined_output.csv', index=False)
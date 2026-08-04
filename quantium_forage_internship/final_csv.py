#this file is to modify the combined csv file to only display pink morsel,
# as well as multiplying the quantity and price and returning a sales column
import pandas as pd

df = pd.read_csv('combined_output.csv')

df['price'] = df['price'].astype(str).str.replace('$', '', regex=False)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

df['sales'] = df['price'] * df['quantity']
df.drop(columns=['price', 'quantity'], inplace=True)

df = df[df["product"].str.startswith("pink morsel", na=False)]

df.to_csv('combined_output.csv', index=False)

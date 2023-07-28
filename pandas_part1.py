import pandas as pd 
# Downlad dataset from Kaggle.com 
# https://www.kaggle.com/datasets/yapwh1208/countries-gdp-2012-to-2021

# Load data from the folder 

df = pd.read_csv('./GDP.csv')
pd.set_option('display.max_columns',64)

# Load
df_start = df.head()
print(df_start)


import pandas as pd


df = pd.read_csv("C:\\Users\\Vflor\Downloads\\sample CSV\\Product_v5.csv")
print(df['value'].sum())
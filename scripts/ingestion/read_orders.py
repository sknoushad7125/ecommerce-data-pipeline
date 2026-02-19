import pandas as pd

df = pd.read_csv("data/raw/orders.csv")

print("Rows:", len(df))
print(df.head())


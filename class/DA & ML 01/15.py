import pandas as pd

df = pd.read_csv("housing.csv")

print(df)
df.info()
print(df.describe())
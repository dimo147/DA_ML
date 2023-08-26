import pandas as pd

df = pd.DataFrame()

df["Age"] = [10,20,30]
df["Department"] = "ICT"
df["AgeDays"] = df["Age"] * 365

print(df)
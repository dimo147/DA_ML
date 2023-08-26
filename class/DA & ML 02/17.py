import pandas as pd

df = pd.read_csv("days.csv")

print(df.groupby("day").sum())


# print(df["sell"][df["day"]==1].sum())
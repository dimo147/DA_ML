import pandas as pd


a = pd.read_csv("a.csv")
b = pd.read_csv("b.csv")


df = pd.DataFrame()
# df.index = list("abcdef")

df["A"] = a["web_traffic"]
df["B"] = b["web_traffic"]


print(df)


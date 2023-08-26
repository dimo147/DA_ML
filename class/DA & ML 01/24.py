import pandas as pd

df = pd.read_csv("BTC-USD.csv")
# df = df.dropna()
# df.dropna(inplace=True)
# df.drop(columns=["Date"],inplace=True)
df["Open"].iloc[100:200].fillna(0, inplace=True)
df.info()

print(df.iloc[360:366])
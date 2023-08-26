import pandas as pd

df = pd.read_csv("BTC-USD.csv")

print(df[df["Open"]>25000])
print(df["Open"].where(df["Open"]> 25000,100,inplace=True))
print(df)
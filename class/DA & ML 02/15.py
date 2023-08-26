import pandas as pd


btc = pd.read_csv("BTC-USD.csv")
eth = pd.read_csv("ETH-USD.csv")


df = pd.DataFrame()
df["Date"] = btc["Date"]
df["BTC_OPEN"] = btc["Open"]
df["ETH_OPEN"] = eth["Open"]


print(df)
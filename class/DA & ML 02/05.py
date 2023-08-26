import pandas as pd


btc_df = pd.read_csv("BTC-USD.csv")


btc_df["Benefit"] = btc_df["Close"] - btc_df["Open"]
print(btc_df)

import numpy as np
import pandas as pd


# btc_df = pd.read_csv("BTC-USD.csv",index_col="Date")
# btc_df["Tarikh"]  = btc_df.index

btc_df = pd.read_csv("BTC-USD.csv")
# btc_df.index = btc_df["Date"]
btc_df.index = np.arange(1000,1366)

btc_df.columns = ["a","b","c","d","e","f","g"]
print(btc_df)


# print(btc_df.iloc[0])
# print(btc_df.loc[["2023-01-01", "2022-12-17"]])
# print(btc_df[["Date","Open","Close"]].loc["2023-01-01": "2023-01-20":3])
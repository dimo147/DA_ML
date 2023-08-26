import numpy as np
import pandas as pd

btc_df = pd.read_csv("BTC-USD.csv")

btc_df.info ()
print(btc_df.describe())


print("-" * 50)

# btc_df["Open"] = pd.to_numeric(btc_df["Open"], errors="raise")
# btc_df["Open"] = pd.to_numeric(btc_df["Open"], errors="ignore")
btc_df["Open"] = pd.to_numeric(btc_df["Open"], errors="coerce")
# btc_df.dropna(inplace=True)
print(btc_df)
btc_df.info ()
print(btc_df.describe())


# Nan dropna fillna
# wrong data type -> convert
# outlier  -> replace drop
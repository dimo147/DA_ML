import numpy as np
import pandas as pd
from persiantools.jdatetime import JalaliDate

btc_df = pd.read_csv("BTC-USD.csv")

btc_df.info ()
print(btc_df.describe())


print("-" * 50)
btc_df["Open"] = pd.to_numeric(btc_df["Open"], errors="coerce")

btc_df["Date"] = pd.to_datetime(btc_df["Date"])
# btc_df["Date"] = JalaliDate(btc_df["Date"])
# btc_df["Date"] = JalaliDate(btc_df["Date"]).month
# btc_df["Date"] = JalaliDate(btc_df["Date"]).week_of_year()
# btc_df["Date"] = JalaliDate(btc_df["Date"]).isoweekday()

print(btc_df)
btc_df.info ()
print(btc_df.describe())



import numpy as np
import pandas as pd
from persiantools.jdatetime import JalaliDate
from datetime import  datetime

# def add_one(x):
#     return x + 1

btc_df = pd.read_csv("BTC-USD.csv")
btc_df["Open"] = pd.to_numeric(btc_df["Open"], errors="coerce")

# btc_df["Jadid"] = add_one(btc_df["Open"])  # Error
# btc_df["Jadid"] = btc_df["Open"].apply(add_one)
# btc_df["Jadid"] = btc_df["Open"].apply(lambda x: x * 2)
btc_df["Jalali"] = btc_df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")))
# btc_df["WeekDay"] = btc_df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")).month)
btc_df["Year"] = btc_df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")).year)
btc_df["WeekOfYear"] = btc_df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")).week_of_year())
btc_df["WeekDay"] = btc_df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")).isoweekday())
# btc_df["Month"] = btc_df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")).strftime("%B"))
btc_df["Month"] = btc_df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")).month)

# d = "2021-12-17"
# print(JalaliDate(datetime.strptime(d, "%Y-%m-%d")))


print(btc_df)

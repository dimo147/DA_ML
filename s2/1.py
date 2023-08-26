import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from persiantools.jdatetime import JalaliDate

data = pd.read_csv("BTC-USD.csv")

data["Jalali"]     = data["Date"].apply(lambda x : JalaliDate(datetime.strptime(x, "%Y-%m-%d")))
data["WeekDay"]    = data["Date"].apply(lambda x : JalaliDate(datetime.strptime(x, "%Y-%m-%d")).weekday()+1)
data["WeekOfYear"] = data["Date"].apply(lambda x : JalaliDate(datetime.strptime(x, "%Y-%m-%d")).week_of_year())
data["Year"]       = data["Date"].apply(lambda x : JalaliDate(datetime.strptime(x, "%Y-%m-%d")).year)
data["Benefit"]    = data["Close"] - data["Open"]
data["Telorance"]  = data["High"] - data["Low"]

# 1
year_1 = data[data["Year"] == 1401][["WeekOfYear", "Benefit"]]
year_2 = data[data["Year"] == 1402][["WeekOfYear", "Benefit"]]
week_benefit_year_1 = (year_1.groupby("WeekOfYear").sum())
week_benefit_year_2 = (year_2.groupby("WeekOfYear").sum())
week_benefit_year = pd.concat([week_benefit_year_1, week_benefit_year_2])
# print(week_benefit_year)
# plt.plot(week_benefit_year)
# plt.show()

# 2

# 3
day = data[["WeekDay", "Telorance"]].groupby("WeekDay").sum()
# print(day)

# 4
data["Date"] = pd.to_datetime(data["Date"])
index = data[(data['Date'] >= '2022-08-06') & (data['Date'] <= '2022-11-02')]

money = 1000

for i, r in index.iterrows():
    if r["WeekDay"] == 1:
        money = money*r["Open"]
    elif r["WeekDay"] == 5:
        r["Close"] / money
    else:
        print(money)

print(index)

# print(index)

# data.info()
# print(data)

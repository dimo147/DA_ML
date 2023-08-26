import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BTC-USD.csv")

# df.info()

# print(df["Open"])

# print(df[["Low","Low", "Low", "High"]])

# print(df.iloc[[1,363,364]])
# print(df.iloc[10:20:2])

# print(df[["Low","High"]].iloc[10:20:2])

# plt.plot(df["Open"].iloc[100:200])
# print(type(df["Open"].iloc[100:200]))
# plt.show()
date = df["Date"]
y = df["Open"]
plt.plot(date, y)

plt.xlabel("Date")
plt.ylabel("Open Price")

plt.xticks(ticks=df["Date"].iloc[::30],rotation=90)

plt.show()
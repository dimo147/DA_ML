import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BTC-USD.csv")
df["Benefit"] = df["Close"] - df["Open"]
df["Tolerance"] = df["High"] - df["Low"]
print(df)

# start = (x1=0, y1=20000)
# end = (x2=365,y2=20000)

# plt.plot(df["Open"], label="Open Price")
#
# # plt.plot([x1,x2],[y1,y2])
# # mean = df["Open"].iloc[330:365].mean()
# mean = df["Open"].mean()
# mn = df["Open"].min()
# mx = df["Open"].max()
#
# plt.plot([0,365],[mean,mean],linestyle="dashed", label="Average")
#
# plt.plot([0,365],[mn,mn],linestyle="dashed", label="Minimum")
# plt.plot([0,365],[mx,mx],linestyle="dashed", label="Maximum")
#
# plt.title("Bitcoin Yearly Open Price")
#
# plt.xlabel("Days")
# plt.ylabel("Open Price")
#
# plt.legend()
# # plt.show()
# plt.savefig("My_Plot.jpg")
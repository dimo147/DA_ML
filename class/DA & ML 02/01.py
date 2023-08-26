import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

btc_df = pd.read_csv("BTC-USD.csv")
open_price = btc_df["Open"]

mean = open_price.mean()

# variance = np.sum(np.power(open_price - mean , 2)) / n

variance = np.var(open_price)
std = np.std(open_price)       # np.sqrt(np.mean(np.power(open_price - mean, 2)))

plt.plot(open_price, label="Open Price")

# plt.plot([0, len(open_price)], [mean, mean], "g--", label="aaaa")
plt.plot([0, len(open_price)], [mean, mean], color="green", linestyle="dashed", label="Mean")
# plt.plot([0, len(open_price)], [mean+(2*std), mean+(2*std)], "b--", label="Up")
# plt.plot([0, len(open_price)], [mean-(2*std), mean-(2*std)], "r--", label="Down")
plt.plot([0, len(open_price)], [mean+std, mean+std], "b--", label="Up")
plt.plot([0, len(open_price)], [mean-std, mean-std], "r--", label="Down")

plt.legend()

plt.show()

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("report.csv", index_col=0)

plt.plot(df["time"], df["score"])
plt.show()

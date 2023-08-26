import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy.signal as signal

# signal.find_peaks()
# signal.findfreqs()

df = pd.read_csv("BTC-USD.csv")

y = df["Open"]
X = np.arange(len(y))

# plt.plot(X,y,label= "Data")


diff = np.diff(y)

# plt.plot(X[1:],diff,label= "Difference")

upper = np.where(diff > 0)[0]
lower = np.where(diff < 0)[0]

plt.plot(X[upper],diff[upper],"g--", label="upper")
plt.plot(X[lower],diff[lower],"r--", label="lower")

peaks_index = signal.find_peaks(y)[0]
# peaks_index = signal.find_peaks_cwt(y,widths=10)[0]
# peaks_index = signal.find_peaks(y,height=1000)[0]
peaks = y.iloc[peaks_index]

# plt.scatter(peaks_index, peaks, color="blue", label="Upper Peaks")
plt.plot(peaks_index, peaks, "y--", label="Upper Peaks")

plt.grid()
plt.show()
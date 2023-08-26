import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("BTC-USD.csv")

y = df["Open"]
X = np.arange(len(y))
plt.plot(X,y, label="True Data")

slope, intercept = np.polyfit (X,y,1)
print(f"{round(slope)} * X + {round(intercept)}")
h = slope * X + intercept
plt.plot(X,h,label="Predict Degree 1")

*slope, intercept = np.polyfit (X,y,2)
print(f"{round(slope[0])} * X^2 + {round(slope[1])} * X + {round(intercept)}")
h = slope[0] * X**2 + slope[1] * X + intercept
plt.plot(X,h,label="Predict Degree 2")

*slope, intercept = np.polyfit (X,y,3)
print(f"{round(slope[0])} * X^3 + {round(slope[1])} * X^2 + {round(slope[2])} * X + {round(intercept)}")
h = slope[0] * X**3 + slope[1] * X**2 + slope[2] * X + intercept
plt.plot(X,h,label="Predict Degree 2")

plt.legend()
plt.show()
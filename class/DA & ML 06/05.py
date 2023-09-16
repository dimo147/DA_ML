import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Data Extraction
from matplotlib import pyplot as plt
from scipy.signal import find_peaks

df = pd.read_csv("EURUSD.csv", index_col="Date")
df.drop(columns=["Adj Close", "Volume"], inplace=True)

y = df["Close"].values
X = np.arange(len(y)).reshape(-1,1)

# Model
model = LinearRegression()

# Train
model.fit(X,y)

# Predict
predict  = model.predict(X)


# Evaluate
# print(model.score(X, y))
print(mean_squared_error(y , predict , squared=False))   # rmse


plt.plot(X, y, label="Data")
plt.plot(X, predict, label="Predict")

plt.legend()
plt.show()

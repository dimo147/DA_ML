import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

rmse_metric = []

df = pd.read_csv("BTC-USD.csv")

y = df["Open"]
X = np.arange(len(y))

fig = plt.figure()

axis = plt.axes(xlim=(X.min(), X.max()),
                ylim=(y.min(), y.max()))

line, = axis.plot([], [], lw=1)
plt.plot(X, y)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    print("i", i)
    coef = 16000 + i * 150
    h = np.full_like(X, coef)
    rmse = np.sqrt(np.mean(np.power(y - h, 2)))
    line.set_data(X, h)
    if len (rmse_metric)<100:
        rmse_metric.append(round(rmse))
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=100, interval=10, blit=True)

plt.show()

plt.plot(rmse_metric)
plt.title("Cost Function")
plt.show()
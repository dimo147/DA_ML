import numpy as np
from matplotlib import pyplot as plt

X = np.ones((1,255))
y = np.arange(100).reshape(100,1)

print(y[1:5])

plt.imshow(X*y,cmap="gray")
plt.show()
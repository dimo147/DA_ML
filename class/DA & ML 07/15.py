import numpy as np
from matplotlib import pyplot as plt

X = np.arange(255).reshape(1,255)
# y = np.arange(100).reshape(100,1)
y = np.ones((100,1))

# plt.imshow(X*y,cmap="gray")
# plt.show()
print(X*y)
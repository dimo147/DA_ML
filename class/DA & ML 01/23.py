import numpy as np
from matplotlib import pyplot as plt

# x = np.random.random(1000)
# x = np.random.randn(1000)

x = np.random.randn(3000)

plt.hist(x)
plt.show()
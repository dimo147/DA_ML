import numpy as np

x = np.array([1,2,3,4,5])
y = np.zeros_like(x)

y[x > 3] = 5

print(x)
print(y)
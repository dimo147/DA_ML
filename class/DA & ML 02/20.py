import numpy as np

x = np.random.randint(1,10,(2,4))
print(x)

print(np.ravel(x))
print(x.reshape(8,))  # ravel
print(x.reshape(-1,8))
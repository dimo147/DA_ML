import numpy as np

x = np.array([[1, 2, 3, 4],
              [4, 5, 6, 4]],dtype=np.float32)
print(x)

# z = np.zeros((x.shape))
# z = np.zeros_like(x)
# print(z)

# o = np.ones((2,3))
# o = np.ones_like(x)
#
# print(o)

# print(np.full((2, 3), 7))
print(np.full_like(x, 3.14))

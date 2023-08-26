import numpy as np

x = np.array([0,127,255], dtype=np.float64)
y = np.array([0,127,255], dtype=np.uint8)

z = x + y
print(z.dtype)
print(z)
import numpy as np

x = np.array([3, 5, 1, 5, 0, 4, 3, 0, 4, 5])

print(x[x>3])           # values
print(np.where(x > 3))  # indexes


# Replace
# x[x>3] = 200
# print(x)

x = np.where(x>3,x,10)
print(x)
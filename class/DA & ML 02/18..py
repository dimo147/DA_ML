import numpy as np

x = np.arange(1,101)


print(x[::10])
print(type(x[::10]))
# print(x[0:10])
# print(x[10:20])
# print(x[20:30])

spl  = np.split(x[2:], 14)
print(type(spl))
print(type(spl[0]))
print(spl[0])
print(spl)
# print(len(x) % 7)
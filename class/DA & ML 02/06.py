import numpy as np

x = np.arange(30)
y = x.reshape((5, 6))

# print(y> 10)
# print(y[y> 10])

y[(y>18) | (y < 5)] = 200

print(y)
# print(np.min(y,axis=1))
# print(np.argmin(y))


# y = x.reshape(7, -1)
# print(np.ravel(y))   #reshape(1,n)
# print(y[1:3,1:4:2])

# x = np.array([2,5,1,4,7])
#
# print(x)
# print(np.diff(np.pad(x, pad_width=(1, 0), mode="constant", constant_values=(0, 0))))

# print(np.pad(x, pad_width=(1, 2), mode="constant", constant_values=(0, 20)))
# print(np.pad(x, pad_width=(1, 2), mode="edge"))
# print(np.pad(x, pad_width=(2, 3), mode="linear_ramp"))

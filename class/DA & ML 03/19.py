import numpy as np


x = np.array([1,2,3,4,5])
# mask = [True,True,False,False,True]
mask = x > 3


print(x[mask])
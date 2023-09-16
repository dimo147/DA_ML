import numpy as np
from sklearn.model_selection import LeaveOneOut

X = np.arange(1, 11)
y = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]

selector = LeaveOneOut()

for split in selector.split(X) :
    print(split)

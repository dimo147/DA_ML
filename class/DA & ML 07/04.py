import numpy as np
from sklearn.model_selection import LeavePOut

X = np.arange(1, 11)
y = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]

selector = LeavePOut(3)
print(selector.get_n_splits(X))

for train,test in selector.split(X) :
    # train
    # test
    # accuracy --> save


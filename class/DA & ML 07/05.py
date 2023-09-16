import numpy as np
from sklearn.model_selection import KFold

X = np.arange(1, 11)
y = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]

selector = KFold(n_splits=5)
print(selector.get_n_splits(X))

for split in selector.split(X) :
    print(split)

import numpy as np
from sklearn.model_selection import train_test_split

X = np.arange(1, 11)
y = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]

for i in range(20):
    x_train, x_test, y_train, y_test = train_test_split(X, y,
                                                        train_size=0.7,
                                                        stratify=y,
                                                        random_state=32)
    print(x_train, x_test)

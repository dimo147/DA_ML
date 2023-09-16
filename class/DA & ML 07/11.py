from sklearn.model_selection import train_test_split

X = [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3],
     [4, 4, 4],
     [5, 5, 5]]

x_train, x_test = train_test_split(X, train_size=0.8)
print(x_train)
print(x_test)
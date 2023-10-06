import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


X,y = make_blobs(centers=2,cluster_std=14,n_features=3,random_state=30)

x_train,x_test,y_train,y_test = train_test_split(X,y,train_size=0.8,stratify=y)

model = SVC()

model.fit(x_train,y_train)

score = model.score(X,y)
train_score = model.score(x_train,y_train)
test_score = model.score(x_test,y_test)


print(score)
print(train_score)
print(test_score)

train_predict = model.predict(x_train)
test_predict = model.predict(x_test)
predict = model.predict(X)

print("Test : ",classification_report(y_test, test_predict))
print("Train : ",classification_report(y_train, train_predict))
print("All : ",classification_report(y, predict))


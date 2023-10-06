import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import decomposition
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import seaborn as sns

data = np.load("mnist.npz")
x_train = data['x_train']
y_train =data['y_train']
x_test = data['x_test']
y_test = data['y_test']

x_train = np.array([np.ravel(x) for x in x_train])
x_test = np.array([np.ravel(x) for x in x_test])

# sns.pairplot(df)
# sns.pairplot(df, kind="kde")
# sns.pairplot(df, kind="hist")

pca = decomposition.PCA(n_components=2)
view = pca.fit_transform(x_train)
plt.scatter(view[:,0], view[:,1], c=y_train, alpha=0.2, cmap='Set1')

plt.legend()
plt.show()

# x_train,x_test,y_train,y_test = train_test_split(X,y,train_size=0.8,stratify=y)
#
# model = SVC()
#
# model.fit(x_train,y_train)
#
# score = model.score(X,y)
# train_score = model.score(x_train,y_train)
# test_score = model.score(x_test,y_test)
#
#
# print(score)
# print(train_score)
# print(test_score)
#
# train_predict = model.predict(x_train)
# test_predict = model.predict(x_test)
# predict = model.predict(X)
#
# print("Test : ",classification_report(y_test, test_predict))
# print("Train : ",classification_report(y_train, train_predict))
# print("All : ",classification_report(y, predict))
#

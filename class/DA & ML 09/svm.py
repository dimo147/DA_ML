import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


X,y = make_blobs(centers=2,cluster_std=14,n_features=3,random_state=30)

x_train,x_test,y_train,y_test = train_test_split(X,y,train_size=0.8,stratify=y)

plt.subplot(1,2,1)
plt.scatter(X[:,0], X[:,1], c=y)

plt.subplot(1,2,2)
clf = SVC(kernel="linear")

clf.fit(x_train,y_train)
predict = clf.predict(x_test)
print(clf.score(x_test,y_test)*100)
print(classification_report(y_test,predict))

predict = clf.predict(X)
plt.scatter(X[:,0], X[:,1], c=predict)
# plot_svc_decision_function(clf)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.scatter(X[:,0],X[:,1], X[:,2], cmap=plt.cm.coolwarm,c=y)

plt.show()
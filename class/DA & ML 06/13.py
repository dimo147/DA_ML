from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

X, y,center = make_blobs(
    n_samples=150,
    n_features=3,
    centers=3,
    cluster_std=17,
    # center_box=[1,10]
    return_centers=True
)

# print(X.shape)   #(sample,feature)
# print(y.shape)   #(class/label)


# plt.scatter(X[:,0], X[:,1],s=X[:,2]*10, c=y,alpha=0.6)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.scatter(center[:, 0], center[:, 1], c="red")
plt.show()

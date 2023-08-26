from matplotlib import pyplot as plt

X = [1, 2, 3, 4, 5, 6, 7]
y_italy = [10, 15, 12, 17, 11, 9, 8]
y_germany = [18,14,12,8,11,12,9]
scale = [1000,1500,500,400,1200,800,300]

# plt.plot(X, y_italy,linestyle="dashed" , color="red", marker="P", label="Italy")
# plt.plot(X,y_germany,"g--P", label="Germany")

plt.scatter(X,y_germany,alpha=0.5,s=scale)
plt.scatter(X,y_italy,alpha=0.5)


# plt.bar(X,y_italy,label="ITALY")
# plt.bar(X,y_germany,label="GERMANY")

plt.xlabel("Days")
plt.ylabel("Infected")

plt.xticks(ticks=[1,3,5,7])

plt.title("Infected in First Week")

# plt.grid()
plt.legend()
plt.show()
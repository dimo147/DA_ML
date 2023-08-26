import pandas as pd

# lambda
# def circle_area(radius):
#     return radius ** 2 * 3.14

c_area = lambda radius: radius ** 2 * 3.14
print(c_area(10))
print(c_area(20))

btc_df = pd.read_csv("BTC-USD.csv")
y = btc_df["Open"]

# y.loc[]
# y.iloc[]

# y.where(c)
# y.apply()

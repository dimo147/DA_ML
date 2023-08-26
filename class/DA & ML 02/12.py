import numpy as np
import pandas as pd

# x = {"numbers": ["10","20","30","40","50","60"]}
x = {"numbers": [10.00001,20,30,40,50,60,2148000000]}

df = pd.DataFrame(x)
df["numbers"] = pd.to_numeric(df["numbers"],errors="coerce",downcast="float")
print(df)
df.info()
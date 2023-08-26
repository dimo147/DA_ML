import pandas as pd

person1 = {"name":"Ali","age":17}
person2 = {"name":"Reza","age":20}

person_list = [person1,person2]

print(person_list)

df = pd.DataFrame(person_list)
print(df)
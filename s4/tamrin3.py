import pandas
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="dimo",
  password="omid7410",
  port = 3306,
  database='bitcoin'
)

curser = db.cursor()

# curser.execute("""
#                 CREATE TABLE history(
#                     Date DATE,
#                     Open DOUBLE,
#                     High DOUBLE,
#                     Low DOUBLE,
#                     Close DOUBLE,
#                     Adj_Close DOUBLE,
#                     Volume DOUBLE
#                 );
# """)

# data = pandas.read_csv("BTC-USD.csv")

# for i in data.values:
#   curser.execute("INSERT INTO history VALUES" + str(tuple(i)))

# db.commit()

curser.execute("SELECT * FROM history;")

for i in curser:
    print(i)

db.close()


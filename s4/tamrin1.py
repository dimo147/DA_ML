import requests as req
from datetime import datetime

API_KEY = "1D870D73-70AC-47A0-AE1A-39E4D189FB6F"

url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"

headers = {
    'X-CoinAPI-Key': API_KEY,
}

inp = input("date in YY/MM/DD: ")
date = datetime.strptime(inp, '%y/%m/%d').strftime('%Y-%m-%d')
print(date)

params = {
    "time": date,
}

response = req.get(url=url, headers=headers, params=params)
data = response.json()

print(data)

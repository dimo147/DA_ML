import requests as req

API_KEY = "e2ac121384b04fbe841182557232408"

url = "http://api.weatherapi.com/v1/forecast.json"

headers = {
    
}

inp = input("Latitude and Longitude seperated with comma: ")

# "48.8567,2.3508" paris

params = {
    "key": API_KEY,
    "q": inp,
}

response = req.get(url=url, headers=headers, params=params)
data = response.json()

print(data)

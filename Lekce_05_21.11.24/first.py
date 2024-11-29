import requests

url = 'https://svatky.adresa.info/json?date=2412'
url2 = 'https://svatky.adresa.info/json?date=3012'

response = requests.get(url2)

print(response)
print(response.url)

data = response.json()
print(data)

{
    "MMDD": [],
    "1224": ['Eva', 'Vášek', 'Štědrý den'],
    "1225": ['Eva', 'Vášek', 'Štědrý den'],
    "1226": []
}
import json, time
import datetime
import requests

def generate_urls():
    d = datetime.date(2000, 1, 1) # datum 1.1.2000
    url = 'https://svatky.adresa.info/json?date='
    url_data = []

    for number in range(14): # 366
        date = d + datetime.timedelta(days=number)
        dm = date.strftime('%d%m')
        url_data.append(url + dm)

    return url_data

def get_data(url):
    response = requests.get(url)
    time.sleep(0.5)
    data = response.json()
    return data

urls = generate_urls()
all_data = {}

for url in urls:
    json_data = get_data(url)

    for item in json_data:
        key = item['date']
        value = item['name']

        if key not in all_data:
            all_data[key] = []

        all_data[key].append(value)

with open('Git_lections/Lekce_06_26.11.24/svatky.json', mode='w', encoding='utf-8') as file:
    json.dump(all_data, file, indent=4)
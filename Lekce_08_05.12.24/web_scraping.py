import re
import requests
import json

rx_pattern = r'<div class="inzeratynadpis">\s*<a href="(.*?)">\s*<img src="(.*?)" class="obrazek" alt="(.*?)">'
rx_bazos = re.compile(rx_pattern)
url = 'https://mobil.bazos.cz/'

response = requests.get(url)

result = rx_bazos.findall(response.text)

# print(result)

data = []
for url, img, title in result:
    item = {'url': url, 'img': img, 'title': title}
    data.append(item)

# print(data)

with open('Git_Lections/Lekce_08_05.12.24/scraped_data.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)
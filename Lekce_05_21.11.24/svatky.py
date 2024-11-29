import datetime

def generate_urls():
    d = datetime.date(2000, 1, 1) # datum 1.1.2000
    url = 'https://svatky.adresa.info/json?date='
    url_data = []

    for number in range(10): # 366
        date = d + datetime.timedelta(days=number)
        dm = date.strftime('%d%m')
        url_data.append(url + dm)

    return url_data

print(generate_urls())
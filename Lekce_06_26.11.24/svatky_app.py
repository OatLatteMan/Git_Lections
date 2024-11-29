import json

with open('Git_lections/Lekce_06_26.11.24/svatky.json', encoding='utf-8') as file:
    data = json.load(file)
    #print(data)

print(data['1101'])

def find_day(name):
    for key, value in data.items():
        if name in value:
            print(key)

find_day('Bohdana')
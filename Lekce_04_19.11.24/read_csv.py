import csv

path  = 'Lekce_04_19.11.24/data.csv'

with open(path, encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        print(line)
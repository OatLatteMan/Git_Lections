# functional_map.py

data = [2, 8, 9]

data2 = [x*x for x in data]
print(data2)

result = map(lambda x: x*x, data)
print(list(result))

def get_pow(cislo):
    return cislo*cislo

result = map(get_pow, data)
print(list(result))
# function.py

data = ['Petr', 'Jan', 'Nina']

def my_func(x):
    return x[-1]

data.sort(key=len) # řazení podle počtu znaků
print(data)

data.sort(key=lambda x: x[-1]) # řazení podle posledního znaknu
print(data)

data.sort(key=lambda x: (len(x), x)) # řazení podle početu a abc
print(data)



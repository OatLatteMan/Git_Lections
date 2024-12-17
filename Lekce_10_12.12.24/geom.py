# geom.py
import math

def get_circle_length(radius):
    result = 2 * math.pi * radius
    return round(result, 2)

test_for_length = {10:62.83, 20:125.66}

for value, result in test_for_length.items():
    assert result == get_circle_length(value)

def get_circle_area(radius):
    result = math.pi*(radius**2)
    return round(result, 2)

test_for_area = {10:314.16, 20:1256.64}

for value, result in test_for_area.items():
    assert result == get_circle_area(value)

data = [{'jmeno':'jakub', 'vek':17}, {'jmeno':'petr', 'vek':19}, {'jmeno':'lena', 'vek':18}] # sortovani podle veku (slozita vlozenost)
data.sort(key = lambda x: x['vek'])
print(data)
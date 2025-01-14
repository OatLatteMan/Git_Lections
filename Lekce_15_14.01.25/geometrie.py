# geometrie.py

def get_triangle_perimeter(a, b , c):
    result = a + b + c

    return result

def is_valid_triangle(a, b, c):
    data = [a, b, c]
    data.sort()
    return (data[0] + data[1]) > data[2]

def get_square_area(a):
    if a <= 0:
        raise ValueError('Strana A musi byt kladna')
    return a*a
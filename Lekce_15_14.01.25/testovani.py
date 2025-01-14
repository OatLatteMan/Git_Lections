"""
1. Manualni
    - alfa - v ramci tymu
    - beta - mimo vyvojovy tym
2. Poluautomaticke

3. Automaticke
    - velka zodpovednost
    - DDT
"""

def get_triangle_perimeter(a, b , c):
    return a+b+c

print(get_triangle_perimeter(10, 10, 10) == 30)
print(get_triangle_perimeter(10, 15, 20) == 45)

def test_get_triangle_perimeter():
    assert get_triangle_perimeter(2, 3, 5) == 10
    assert get_triangle_perimeter(10, 10, 10) == 20

test_get_triangle_perimeter()
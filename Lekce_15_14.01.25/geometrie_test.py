# geometrie_test.py

import unittest
import geometrie as g

# obvod, obsah kruhu
# trojuhelnikova nerovnost
# objem cylindru

class Test_geometrie(unittest.TestCase):
    def test_get_triangle_perimeter(self):
        result = g.get_triangle_perimeter(10, 40, 33)
        self.assertEqual(result, 83)

    def test_triangle_validity(self):
        pass

    def test_get_circle_perimeter(self):
        pass

    def test_get_circle_area(self):
        pass

    def test_cone_volume(self):
        pass

unittest.main()
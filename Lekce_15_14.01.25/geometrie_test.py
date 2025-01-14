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

    def test_is_valid_triangle_10_10_10(self):
        result = g.is_valid_triangle(10, 10, 10)
        self.assertTrue(result)

    def test_is_valid_triangle_10_10_100(self):
        result = g.is_valid_triangle(10, 10, 100)
        self.assertFalse(result)

    def test_isvalid_triangle_10_10_n10(self):
        result = g.is_valid_triangle(10, 10, -10)
        self.assertFalse(result)

    def test_get_square_area_10(self):
        result = g.get_square_area(10)
        self.assertEqual(result, 100)

    def test_get_square_area_1000(self):
        result = g.get_square_area(1000)
        self.assertEqual(result, 1000000)

    def test_get_square_area_n10(self):
        with self.assertRaises(ValueError):
            g.get_square_area(-10)

    def test_get_circle_perimeter(self):
        pass

    def test_get_circle_area(self):
        pass

    def test_cone_volume(self):
        pass

unittest.main()
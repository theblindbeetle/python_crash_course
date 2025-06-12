"""
NOTE: This is activity is based on the already developed 11.1
"""

import unittest
from city_functions import place

class PlaceTest(unittest.TestCase):
    """Test for 'city_functions.py'."""

    def test_city_country(self):
        """Do strings like 'City, Country' work?"""
        formatted_place = place('santiago', 'chile')
        self.assertEqual(formatted_place, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do strings like 'City, Country - population 5000000' work?"""
        formatted_place = place(
            'santiago', 'chile', 5000000)
        expected = 'Santiago, Chile - population 5000000'
        self.assertEqual(formatted_place, expected)

if __name__ == '__main__':
    unittest.main()
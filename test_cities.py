import unittest
from city_functions import get_city_country

class NamesTestCase(unittest.TestCase):
    '''测试city_functions.py'''
    def test_city_country(self):
        formatted_name1 = get_city_country('santiago','chile')
        self.assertEqual(formatted_name1,'Santiago,Chile')

    def test_city_country_population(self):
        formatted_name2 = get_city_country('santiago','chile',str(5000000))
        self.assertEqual(formatted_name2,'Santiago,Chile-Population=5000000')


unittest.main()
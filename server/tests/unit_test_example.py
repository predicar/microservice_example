"""The file contains a test for each function in the example_service.py"""

import unittest
from server.services.example_service import get_value_by_key


class UnitTestExample(unittest.TestCase):
    def test_get_value_by_key(self):
        dictionary = {'color': 'blue', 'year': 2020}
        self.assertEqual(2020, get_value_by_key(dictionary=dictionary, key='year'))
        self.assertNotEqual(2020, get_value_by_key(dictionary=dictionary, key='color'))
        self.assertRaises(KeyError, get_value_by_key, dictionary=dictionary, key='address')


if __name__ == '__main__':
    unittest.main()

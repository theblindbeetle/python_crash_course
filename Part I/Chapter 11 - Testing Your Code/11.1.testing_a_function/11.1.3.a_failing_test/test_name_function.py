import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Eleanor Rigby' work?"""
        formatted_name = get_formatted_name('eleanor', 'rigby')
        self.assertEqual(formatted_name, 'Eleanor Rigby')

if __name__ == '__main__':
    unittest.main()
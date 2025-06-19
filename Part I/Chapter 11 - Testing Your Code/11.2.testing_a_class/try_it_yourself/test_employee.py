import unittest
from employee import Employee

class TestEmployeeRise(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """Create an employee and setup custom increments."""
        self.base_salary = 100_000
        self.employee = Employee("Potato", "Head",
                            self.base_salary)
        self.increments = [5_000, 10_000, 15_000]

    def test_give_default_raise(self):
        """Test that the default rise is properly given."""
        self.assertEqual(self.base_salary+5_000, self.employee.give_raise())

    def test_give_custom_raise(self):
        """Test that a custom raise is properly given."""
        for increment in self.increments:
            self.assertEqual(self.base_salary+increment, self.employee.give_raise(increment))

if __name__ == '__main__':
    unittest.main()
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # --- Division Tests ---
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)

    def test_division_result_fraction(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))  # expecting None

if __name__ == "__main__":
    unittest.main()

import unittest
from functions_to_test import Calculator


class TestForCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(8, 12), 20)
        self.assertEqual(Calculator.add(7, 4), 11)
        self.assertEqual(Calculator.add(16, 7), 23)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(5, 4), 1)
        self.assertEqual(Calculator.subtract(19, 9), 10)
        self.assertEqual(Calculator.subtract(23, 7), 16)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(13, 5), 65)
        self.assertEqual(Calculator.multiply(9, 18), 162)
        self.assertEqual(Calculator.multiply(8, 6), 48)

    def test_divide(self):
        self.assertEqual(Calculator.divide(35, 5), 7)
        self.assertEqual(Calculator.divide(42, 7), 6)
        self.assertRaises(ValueError, lambda: Calculator.divide(6, 0))

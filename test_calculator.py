import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        super().setUp()

    def test_addition_operator(self):
        calculator = self.calculator
        res = calculator.add(1, 2)
        self.assertEqual(3, res)

    def test_subtraction_operator(self):
        calculator = self.calculator
        res = calculator.subtract(4, 2)
        self.assertEqual(2, res)

    def test_multiplication_operator(self):
        calculator = self.calculator
        res = calculator.multiply(10, 3)
        self.assertEqual(30, res)

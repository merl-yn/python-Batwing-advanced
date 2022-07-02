import pytest
from functions_to_test import Calculator


class TestForCalculator:

    def test_add(self):
        assert Calculator.add(8, 12) == 20
        assert Calculator.add(7, 4) == 11
        assert Calculator.add(16, 7) == 23

    def test_subtract(self):
        assert Calculator.subtract(5, 4) == 1
        assert Calculator.subtract(19, 9) == 10
        assert Calculator.subtract(23, 7) == 16

    def test_multiply(self):
        assert Calculator.multiply(13, 5) == 65
        assert Calculator.multiply(9, 18) == 162
        assert Calculator.multiply(8, 6) == 48

    def test_divide(self):
        assert Calculator.divide(35, 7) == 5
        assert Calculator.divide(42, 7) == 6
        with pytest.raises(ValueError):
            Calculator.divide(6, 0)

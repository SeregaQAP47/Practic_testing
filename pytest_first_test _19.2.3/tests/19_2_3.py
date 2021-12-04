import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiplay_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiplay_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction(self):
        assert self.calc.subtraction(self, 8, 2) == 6

    def test_adding(self):
        assert self.calc.adding(self, 7, 9) == 16
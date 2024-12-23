"""Sample testcase
"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """Test calc module"""

    def test_add_numbers(self):
        """Add numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Subtract numbers"""
        res = calc.subtract(10, 20)
        self.assertEqual(res, 10)

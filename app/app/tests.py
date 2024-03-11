"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Tes adding number together"""
        res = calc.add(3, 4)
        self.assertEquals(res, 7)

    def test_subtract_numbers(self):
        res = calc.subtract(7, 5)
        self.assertEqual(res, 2)

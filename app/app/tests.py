""" sample testcase
"""
from django.test import SimpleTestCase
from app import calc
class calctest(SimpleTestCase):
    """ test calc module"""
    def test_add_numbers(self):
        """ add numbers"""
        res=calc.add(5,6)
        self.assertEqual(res,11)
    def test_subtract_number(self):
        res=calc.subtract(10,20)    
        self.assertEqual(res,10)
        
import unittest
from math import pi
from circle import circle_area


class TestCaseCircle(unittest.TestCase):
    def test_area(self):
        # test area when if area >=0:
        self.assertAlmostEqual(circle_area(1) , pi )
        self.assertAlmostEqual(circle_area(0) , 0 )
        self.assertAlmostEqual(circle_area(2.1) , pi*2.1**2 )
    
    def test_value(self):
        # make sure the value error are raise when needed
        self.assertRaises(ValueError,circle_area,-2)

    def test_type(self):
        # make sure the type error are raise when needed
        self.assertRaises(TypeError,circle_area,3+5j)
        self.assertRaises(TypeError,circle_area,True)
        self.assertRaises(TypeError,circle_area,"True")














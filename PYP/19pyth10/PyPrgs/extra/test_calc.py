#!/usr/bin/python3
""" Test the module calc and in there the function calc """

import unittest
import calc

class CalcTest(unittest.TestCase):
    "test class for calc.calc"

    def setUp(self):
        "before each test"
        pass

    def test_calc(self):
        "function calc exists"
        self.assertTrue("calc" in dir(calc))

    def test_calc_add(self):
        "addition"
        self.assertEqual(3.0, calc.calc("1", "+", "2"))

    def test_calc_sub(self):
        "subtraction"
        self.assertEqual(2.0, calc.calc("3", "-", "1"))

    def test_calc_mul(self):
        "multiplication"
        self.assertEqual(6.0, calc.calc("2", "*", "3"))

    def test_calc_div(self):
        "division"
        self.assertEqual(2.0, calc.calc("6", "/", "3"))

    def test_calc_add_multi(self):
        "add many different combinations"
        for x in range(1, 10):
            for y in range(1, 10):
                erg = calc.calc(str(x), "+", str(y))
                self.assertEqual(float(x+y), erg)

    def test_calc_number_fail(self):
        "conversion error on numbers"
        try:
            erg = calc.calc("bla", "+", "schlonz")
            if isinstance(erg, (int, float)):
                self.fail("must not succeed")
        except:
            pass

    def test_calc_op_fail(self):
        "no result on unknown op"
        try:
            erg = calc.calc("1", "?", "2")
            if isinstance(erg, (int, float)):
                self.fail("must not succeed")
        except:
            pass

if __name__ == '__main__':
    unittest.main()

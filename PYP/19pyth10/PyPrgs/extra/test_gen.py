#!/usr/bin/python3
"""Test der Generatorimplementierung"""

from __future__ import generator_stop # do check py 3.7

import unittest
from itertools import islice
import gen
import pp

class TestGen(unittest.TestCase):
    "Testen der Generatorimplementierung"

    def test_prim(self):
        "Generator Primzahlen"
        explis = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        lis = list(islice(pp.prim(), 0, 10))
        self.assertEqual(explis, lis)

    def test_pprim(self):
        "Generator Primzahlzwillinge"
        explis = [(11, 13), (17, 19), (29, 31), (41, 43)]
        lis = list(islice(pp.pprim(), 2, 6))
        self.assertEqual(explis, lis)

    def test_abwechselnd(self):
        "Generator abwechselnd"
        explis = [0, 10, 1, 11, 2, 12]
        lis = list(gen.abwechselnd(iter(range(3)), iter(range(10, 13))))
        self.assertEqual(explis, lis)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGen))
    unittest.TextTestRunner(verbosity=2).run(suite)

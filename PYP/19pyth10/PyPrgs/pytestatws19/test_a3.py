#!/usr/bin/python3
"Testet die Generatoren ith und secondonly aus a3"
from itertools import islice
import operator
import unittest

import a3

class TestA3(unittest.TestCase):
    "Tests der Funktionen aus a3"

    def test_ith(self):
        "ith mit einfachen Beispielen und ein größeres"
        lis = [1, 2, 3]
        got = list(a3.ith((i for i in lis)))
        self.assertEqual([1, 3], got)
        lis = [1, 2, 3, 4, 5]
        got = list(a3.ith((i for i in lis)))
        self.assertEqual([1, 3], got)
        lis = [1, 2, 3, 4, 5, 6]
        got = list(a3.ith((i for i in lis)))
        self.assertEqual([1, 3, 6], got)
        got = list(a3.ith((i for i in list(range(1, 19)))))
        self.assertEqual([1, 3, 6, 10, 15], got)
        got = list(a3.ith((i for i in list(range(1, 10000)))))[-5:]
        self.assertEqual([9316, 9453, 9591, 9730, 9870], got)

    def test_secondonly1(self):
        "second only mit einfachen Beispielen"
        lis = [1, 2, 1]
        got = list(a3.secondonly((e for e in lis)))
        self.assertEqual([1], got)
        lis = [1, 2, 3]
        got = list(a3.secondonly((e for e in lis)))
        self.assertEqual([], got)
        lis = [1, 2, 2, 1]
        got = list(a3.secondonly((e for e in lis)))
        self.assertEqual([2, 1], got)
        lis = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 3, 5, 4, 2, 5, 1, 3, 2, 4]
        got = list(a3.secondonly((e for e in lis)))
    
    def test_secondonly2(self):
        "second only mit unendlichen Generatoren"
        from itertools import islice
        got = list(islice(a3.secondonly(r()), 0, 1))
        self.assertEqual([44], got)
        got = list(islice(a3.secondonly(r()), 0, 2))
        self.assertEqual([44, 16], got)
        got = list(islice(a3.secondonly(r(1, 2**20)), 1000, 1003))
        self.assertEqual([638079, 167752, 9529], got)
        gen = a3.secondonly(c(17))
        val = next(gen) # do not call next again, endless!
        self.assertEqual(17, val)

def c(val=0):
    "unendliche Sequez eines konstanten Werts"
    while True:
        yield val

def r(fro=1, to=100):
    "unendliche Sequenz von (Pseudo-)Zufallszahlen, bei jedem Aufruf gleich"
    import random
    random.seed(4217)
    while True:
        yield random.randint(fro, to)


if __name__ == '__main__':
    unittest.main()

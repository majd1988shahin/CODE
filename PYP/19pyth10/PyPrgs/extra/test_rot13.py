#!/usr/bin/python3
"""check the rot13 algorithm"""

import unittest

from rot13 import rot13


class Rot13Test(unittest.TestCase):
    "test class for ro13.rot13"

    def test_basics(self):
        "basics"
        self.assertEqual("abcdefghijklm", rot13("nopqrstuvwxyz"))
        self.assertEqual("ABCDEFGHIJKLM", rot13("NOPQRSTUVWXYZ"))
        self.assertEqual("nopqrstuvwxyz", rot13("abcdefghijklm"))
        self.assertEqual("NOPQRSTUVWXYZ", rot13("ABCDEFGHIJKLM"))

    def test_nonascii(self):
        "nonascii"
        self.assertEqual("0123456789", rot13("0123456789"))
        self.assertEqual(" ,;.-?=)(/&%$§!", rot13(" ,;.-?=)(/&%$§!"))

    def test_example(self):
        "beispiel"
        self.assertEqual("Clguba vfg gbyy!", rot13("Python ist toll!"))

    def test_twice(self):
        "zweimal..."
        texts = [
            "Hello Python World",
            "To Be or Not To Be",
            "2b|!2b",
            """How do you keep a blonde busy for two days?
Tvir ure n cvrpr bs cncre gung unf "cyrnfr ghea bire"
jevggra ba obgu fvqrf.""",
            """What is it called when a blonde dies her hair brown?
Negvsvpvny vagryyvtrapr. """,
            """Wie bringt man die Augen einer Blondine zum leuchten?
Gnfpuraynzcr vaf Bue. """,
            """How to drown a blonde?
Zbhag gur zveebe ng gur cbby'f obggbz."""
            ]
        for text in texts:
            self.assertEqual(text, rot13(rot13(text)))

if __name__ == '__main__':
    unittest.main()

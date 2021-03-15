#!/usr/bin/python3
"""check the soundex algorithm"""

import unittest
from soundex import soundex

class SoundexTest(unittest.TestCase):
    "test class for soundex.soundex"

    def test_examples(self):
        "examples"
        self.assertEqual("s53200", soundex("soundex"))
        self.assertEqual("s53200", soundex("soundeggs"))
        self.assertEqual("f46140", soundex("flurbel"))

    def test_singles(self):
        "single characters"
        self.assertEqual("a00000", soundex("a"))
        self.assertEqual("x00000", soundex("x"))
        self.assertEqual("o00000", soundex("o"))

    def test_upperchars(self):
        "also uppercase characters"
        self.assertEqual("s53200", soundex("Soundex"))
        self.assertEqual("s53200", soundex("soUNDeggs"))
        self.assertEqual("f46140", soundex("fLuRbEl"))

    def test_tooooolong(self):
        "more than 6 chars"
        self.assertEqual("s53232", soundex("soundexdex"))
        self.assertEqual("s53232", soundex("soundexdexdex"))
        self.assertEqual("s53232", soundex("soundexdexdexdex"))
        self.assertEqual("s53232", soundex("soundexdexdexdexflurbel"))

    def test_short(self):
        "long words shortened a lot"
        self.assertEqual("s00000", soundex("sAEIOUWYHaeiouwyh"))
        self.assertEqual("x00000", soundex("x" + "AEIOUWYHaeiouwyh"*17))
        self.assertEqual("a00000", soundex("a" + "AEIOUWYHaeiouwyh"*42))

    def test_all(self):
        "all characters"
        chars = "AEIOUWYHaeiouwyh".join("bfpvCGJKQSXZBFPVcgjkqsxzdt")
        self.assertEqual("s12123", soundex("s" + chars))
        chars = "AEIOUWYHaeiouwyh".join("lmnrmnrmnrmnrmnrmnr")
        self.assertEqual("x45656", soundex("x" + chars))


if __name__ == '__main__':
    unittest.main()

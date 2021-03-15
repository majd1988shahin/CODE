#!/usr/bin/python3
"test regular expressions"

import unittest

import regexe


class RegexeTest(unittest.TestCase):
    "test the regular expressions"

    @classmethod
    def setUpClass(cls):
        "just once for the class!"
        cls.SOL = regexe.SOL
        cls.DIC = regexe.read_checks(regexe.CHECKFILE)

    def test_plz(self):
        "Postleitzahlen"
        regtype = "PLZ"
        # could all be done in one
        regex = self.SOL[regtype]
        for tocheck, okay in self.DIC[regtype]:
            res = regexe.check(regex, tocheck, okay, verbose=False)
            msg = "%s on %s expect %s got %s" % (regex, tocheck, okay, not okay)
            self.assertTrue(res, msg)

    def _doit(self, regtype):
        # print("Testing %s" % regtype)
        regex = self.SOL[regtype]
        for tocheck, okay in self.DIC[regtype]:
            res = regexe.check(regex, tocheck, okay, verbose=False)
            msg = "%s on %s expect %s got %s" % (regex, tocheck, okay, not okay)
            self.assertTrue(res, msg)

    def test_datum(self):
        "Datum"
        self._doit("Datum")

    def test_eur(self):
        "Euro"
        self._doit("EUR")

    def test_tel(self):
        "Telefonnummern"
        self._doit("Tel")

    def test_email(self):
        "Email"
        self._doit("Email")


if __name__ == '__main__':
    unittest.main()

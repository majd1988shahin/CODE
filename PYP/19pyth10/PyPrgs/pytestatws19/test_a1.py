#!/usr/bin/python3
"Testet die Funktionen encrypt und decrypt im Modul a1"
import unittest
import a1


class TestA1(unittest.TestCase):
    "Test der Funktionen aus a1"

    def test_enc1(self):
        "just encrypting small examples"
        encrypted = a1.encrypt("abcde", "abc")
        self.assertEqual("acedf", encrypted)
        encrypted = a1.encrypt("abcxyz", "ab")
        self.assertEqual("accyya", encrypted)

    def test_enc2(self):
        "a little larger"
        encrypted = a1.encrypt("aberhalloundso", "a")
        self.assertEqual("aberhalloundso", encrypted)
        encrypted = a1.encrypt("aberhalloundso", "ab")
        self.assertEqual("aceshblmovnesp", encrypted)
        encrypted = a1.encrypt("aberhalloundso", "abc")
        self.assertEqual("acgriclmquofsp", encrypted)

    def test_encdec1(self):
        "both ways"
        decrypted = a1.decrypt("aberhalloundso", "a")
        self.assertEqual("aberhalloundso", decrypted)
        decrypted = a1.decrypt("aberhalloundso", "ab")
        self.assertEqual("aaeqhzlkotncsn", decrypted)
        decrypted = a1.decrypt("aberhalloundso", "abc")
        self.assertEqual("aacrgylkmumbsn", decrypted)
        enc1 = a1.encrypt("a", "abcdefgh")
        self.assertEqual("a", enc1)
        enc2 = a1.encrypt("ab", "abcdefgh")
        self.assertEqual("ac", enc2)
        enc3 = a1.encrypt("abc", "abcdefgh")
        self.assertEqual("ace", enc3)
        dec1 = a1.decrypt("a", "abcdefh")
        self.assertEqual("a", dec1)
        dec2 = a1.decrypt("ab", "abcdefgh")
        self.assertEqual("aa", dec2)

    def test_encdec2(self):
        "typical larger texts"
        text, secret, enc = ("hesdeadjim", "mccoysttos", "tgurcswcwe")
        encrypted = a1.encrypt(text, secret)
        self.assertEqual(enc, encrypted)
        orig = a1.decrypt(encrypted, secret)
        self.assertEqual(text, orig)
        text, secret, enc = ("nomatterwhereyougothereyouare", "buckaroobanzai",
                             "oioktksfxhrqegpoiytysffybtazf")
        encrypted = a1.encrypt(text, secret)
        self.assertEqual(enc, encrypted)
        orig = a1.decrypt(encrypted, secret)
        self.assertEqual(text, orig)
        text, secret, enc = ("withgreatpowertheremustalsocomegreatresponsibility", "stanlee",
                             "obturvismpbhivlaeepqykmaydsggfetcielkefasrkbbvwmxq")
        encrypted = a1.encrypt(text, secret)
        self.assertEqual(enc, encrypted)
        orig = a1.decrypt(encrypted, secret)
        self.assertEqual(text, orig)
        text, secret, enc = ("greetingsmyfriendweareallinterestedinthefutureforthatiswhereyouandiaregoingtospendtherestofourlivesandremembermyfriendfutureeventssuchasthesewillaffectyouinthefuture", "criswellplanninefromouterspace",
                             "iimwpmyrhxyseqrrinsmfytpcactgvgjbwzmyewpfhgceikfffvummjowetiafcsjhtlgpgbvvtxtjdqbxmlvjtsvshfcjhmgphlnqemzirssdasyvzwcdhyvlzwazpyidshppnwyysesqbpcsufggvpwmerestqughzr")
        encrypted = a1.encrypt(text, secret)
        self.assertEqual(enc, encrypted)
        orig = a1.decrypt(encrypted, secret)
        self.assertEqual(text, orig)

if __name__ == '__main__':
    unittest.main()

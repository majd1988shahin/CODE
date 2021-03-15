import unittest
import sys
import os
import checkblock as cb

class TestCheckBlock(unittest.TestCase):

    

    def test_1(self):
        code=cb.codeVonFilename("sample1")    
        self.assertEqual(cb.checkblock(code),(None,None,None))

    def test_2(self):
        code=cb.codeVonFilename("sample2")    
        self.assertEqual(cb.checkblock(code),(5, '}', 'extra Klammer'))

    def test_3(self):
        code=cb.codeVonFilename("sample3")    
        self.assertEqual(cb.checkblock(code),(5, '}', 'extra Klammer'))

    def test_4(self):
        code=cb.codeVonFilename("sample4")    
        self.assertEqual(cb.checkblock(code),(3, '{', 'Klammer ist nicht geschlossen'))

    def test_5(self):
        code=cb.codeVonFilename("sample5")    
        self.assertEqual(cb.checkblock(code),(3, '(', 'Klammer ist nicht geschlossen'))

    def test_6(self):
        code=cb.codeVonFilename("sample6")    
        self.assertEqual(cb.checkblock(code),(4, '(', 'Klammer ist nicht geschlossen')
)
    
    def test_7(self):
        code=cb.codeVonFilename("sample7")    
        self.assertEqual(cb.checkblock(code),(4, '{', 'Klammer ist nicht geschlossen'))
    
    def test_8(self):
        code=cb.codeVonFilename("sample8")    
        self.assertEqual(cb.checkblock(code),(4, '{', 'Klammer ist nicht geschlossen'))
    
    def test_9(self):
        code=cb.codeVonFilename("sample9")    
        self.assertEqual(cb.checkblock(code),(4, '{', 'Klammer ist nicht geschlossen')
)

    

if __name__ == '__main__':
    unittest.main()
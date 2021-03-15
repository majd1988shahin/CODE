import unittest
import sys
import os
import soundex as sdx

class TestCheckBlock(unittest.TestCase):
    def test_1(self):  
        self.assertEqual(sdx.soundex("soundex"),"S53200")
    
    def test_2(self):  
        self.assertEqual(sdx.soundex("soundeggs"),"S53200")
    
    def test_3(self):  
        self.assertEqual(sdx.soundex("flurbel"),"F46140")
    
  

if __name__ == '__main__':
    unittest.main()
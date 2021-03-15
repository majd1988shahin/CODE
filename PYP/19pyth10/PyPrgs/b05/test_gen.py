import unittest
from gen import Gen
from itertools import islice

class Test(unittest.TestCase):
    

    def test_gen1(self):
        G=Gen()
        gen=G.g1()
        
        x=list(islice(gen,0,10))
        self.assertEqual(x,[i for i in range(1,11)])
    def test_gen2(self):
        G=Gen()
        gen=G.g2()
        x=list(islice(gen,0,10))
        self.assertEqual(x,[i**2 for i in range(1,11)])
    
    def test_abwachsel(self):
        G=Gen()
        gen1,gen2=G.g1(),G.g2()
        gen_abwachs=G.abwechselnd(gen1,gen2)
        x=list(islice(gen_abwachs,0,10))
        y=[]
        for i in range(1,6):
            y.append(i)
            y.append(i**2)
        self.assertEqual(x,y)
    def test_prim(self):
        from pp import prim
        gen =prim()
        x=list(islice(gen,0,7))
        y=[2, 3, 5, 7, 11, 13, 17]
        self.assertEqual(x,y)
    def test_pprim(self):
        from pp import pprim
        gen=pprim()
        x=list(islice(gen,0,5))
        y=[(3, 5), (5, 7), (11, 13), (17, 19), (29, 31)]
        self.assertEqual(x,y)
if __name__=="__main__":
    unittest.main()
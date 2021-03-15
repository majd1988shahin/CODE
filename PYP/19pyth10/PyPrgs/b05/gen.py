class Gen:
    
    def abwechselnd(self,gen1,gen2):
        while 1:
            yield next(gen1)
            yield next(gen2)
    
    def g1(self):
        self.i=1
        while 1:
            yield self.i
            self.i=self.i+1
    
    
    def g2(self):
        self.i2=1
        while 1:
            yield self.i2**2
            self.i2+=1
       
    def run(self):
        a,b=self.g1(),self.g2()
        G=self.abwechselnd(a,b)
        for i in range(10):
            print(next(G))
        
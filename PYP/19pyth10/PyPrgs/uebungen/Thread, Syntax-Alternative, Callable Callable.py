import threading
class IthPrime(threading.Thread):
    def __init__(self,i,callback=None):
        super().__init__()
        self.i=i
        assert self.i>0
        self.ith_prime=None
        self.callback=callback
    def is_prime(self,x):
        return [div for div in range(2,x) if x%div==0]==[]
    def prime_gen(self):
        yield 2
        p=3
        while True:
            if self.is_prime(p): yield p
            p+=2
    def run(self):
        pg=self.prime_gen()
        for _ in range(self.i-1):
            next(pg)
        self.ith_prime=next(pg)
        print("{0}. Prime ist {1}".format(self.i,self.ith_prime))
        if self.callback :self.callback(self.ith_prime)
"""result=None
p=IthPrime(1780,callback =lambda x:print("callback ",x))
p.start()"""
##################################
class IthPrimeCallable():
    def __init__(self,i,callback=None):
        super().__init__()
        self.i=i
        assert self.i>0
        self.ith_prime=None
        self.callback=callback
    def is_prime(self,x):
        return [div for div in range(2,x) if x%div==0]==[]
    def prime_gen(self):
        yield 2
        p=3
        while True:
            if self.is_prime(p): yield p
            p+=2
    def __call__(self):
        pg=self.prime_gen()
        for _ in range(self.i-1):
            next(pg)
        self.ith_prime=next(pg)
        print("{0}. Prime ist {1}".format(self.i,self.ith_prime))
        if self.callback :self.callback(self.ith_prime)

"""ithprimecallable =IthPrimeCallable(1781)
thread1=threading.Thread(target=ithprimecallable)
thread1.start()"""


iv=[1700 , 1701,1702]

ipts=[IthPrime(i) for i in range(1700,1701)]
print(ipts)
for ipt in ipts:
    ipt.start()

import time

time.sleep(10)
for ipt in ipts:
    print(ipt.i,ipt.ith_prime)

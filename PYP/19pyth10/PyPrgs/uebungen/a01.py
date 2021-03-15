is_prime=(lambda x: [i for i in range(2,x) if x%i==0]==[])

def prim_gen():
    yield 2
    p=3
    while True:
        if is_prime(p):
            yield p
        p+=2
f=prim_gen()
#print([next(f) for _ in range(15)])

import threading

class IthPrime(threading.Thread):
    def __init__(self,i,callback):
        super().__init__()
        self.callback=callback
        self.i=i
        assert self.i >0
        self.ith_prime=None

    def run(self):
        p=prim_gen()
        for _ in range(self.i-1):
            next(p)
        self.ith_prime=next(p)
        self.callback(self.i,self.ith_prime)
        print("done: %d is %d"%(self.i,self.ith_prime))

r=[]
def get_res(i,v):
    r.append((i,v))
i=171
ipt=IthPrime(i,lambda i,v: r.append((i,v)))
ipt.start()
i=200
ipt2=IthPrime(i,get_res)
ipt2.start()
import time
time.sleep(2)
print("result :{0}".format(r))

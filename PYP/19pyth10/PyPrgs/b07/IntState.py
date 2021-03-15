import threading , time,random
from threading import Event
class IntState():
    def __init__(self):
        self.v=0
    
    def activ(self,s):
        self.v+=s
    @property 
    def value(self):
        return self.v
    
class IntStateSafe:
    def __init__(self):
        self.v=0
        self.lock=threading.Lock()
        
    def activ(self,s):
        with self.lock:
            self.v+=s
    @property
    def value(self):
        with self.lock:
            return self.v
    
class state(threading.Thread):
    def __init__(self,IS,Max):
        self.thl=[]
        self.IS=IS
        self.Max=Max
       # self.stop=threading.Event()
        self.v=0
        super().__init__()
    def join(self):
        #self.stop.set()
        super().join()
    def run(self):
        for _ in range(self.Max):
            #if self.stop.is_set(): break
            s=random.randint(0,100)
            self.IS.activ(s)
            self.v+=s

IS=IntState()
ths=[]
n=17
for i in range(n):
    ths.append(state(IS,100000))
t1=time.process_time() 
for th in ths:
    th.start()
#time.sleep(3)
result=0
for th in ths:
    th.join()
    result+=th.v
t2=time.process_time()
print("unsicher ergibnis :",IS.value,"Reale Ergibnis ",result) # 
print("Es dauert :",t2-t1)
################
################safe###############
ISS=IntStateSafe()
ths=[]
n=17
for i in range(n):
    ths.append(state(ISS,100000))
for th in ths:
    th.start()
#time.sleep(3)
result=0
for th in ths:
    th.join()
    result+=th.v
t3=time.process_time()
print("Sicher ergibnis :",ISS.value,"Reale Ergibnis ",result) 
print("Es dauert :",t3-t2)
"""unsicher ergibnis : 52126033 Reale Ergibnis  85013131
Es dauert : 6.696820499
Sicher ergibnis : 85080905 Reale Ergibnis  85080905
Es dauert : 33.173647009999996"""
import threading , time,random
from threading import Event

class cha(threading.Thread):
    def __init__(self,chr,Queue,lock):
        self.chr=chr
        self.Queue=Queue
        self.stop=Event()
        self.lock=lock
        super().__init__()
    def join(self):
        self.stop.set()
        super().join()
    def run(self):
        while not self.stop.is_set():
            t=random.random()/100
            time.sleep(t)
            with self.lock:
                if len(self.Queue)==0:                
                    self.Queue.append(self.chr)

class entscheider(threading.Thread):
    def __init__(self,Queue,lock,ths,how_many=100):
        self.Queue=Queue
        self.lock=lock
        self.stop=Event()
        self.ths=ths
        self.how_many=how_many
        self.dic={chr(i):0 for i in range(ord("a"),ord("a")+26)}
        super().__init__()
        

    def join(self):
        self.stop.set()
        super().join()
    def run(self):
        while not self.stop.is_set():
            a=None
            with self.lock:
                if self.Queue:
                    a=self.Queue.pop(0)
            if a is not None:
                self.dic[a]+=1
                if self.dic[a]>=self.how_many:
                    print(a," hat gewonnen")
                    self.stop.set()
                    for th in self.ths:
                        th.join()
                    

Queue=[]
ths=[]
lock=threading.Lock()
for i in range(ord("a"),ord("a")+26):
    ths.append(cha(chr(i),Queue,lock))

ent=entscheider(Queue,lock,ths)
ent.start()
random.shuffle(ths)
for th in ths:
    th.start()

while not ent.stop.is_set():
    time.sleep(0.2)
ent.join()
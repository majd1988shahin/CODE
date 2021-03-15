import threading ,time
from threading import Condition

class Producer(threading.Thread):
    def __init__(self,queue,cond,howmany=5):
        self.queue=queue
        self.cond=cond
        self.howmany=howmany
        super().__init__()
    def run(self):
        for i in range(self.howmany,0,-1):
            cond.acquire()
            self.queue.append(i)
            print("set%d"%i)
            self.cond.notify()
            self.cond.release()
            time.sleep(0.00001)
        print("Producer is done")

class Consumer(threading.Thread):
    def __init__(self,queue,cond):
        self.queue=queue
        self.cond=cond
        self.done=threading.Event()
        self.sum=0
        self.misses=0
        super().__init__()
    def join(self):
        self.done.set()
        super().join()
    def run(self):
        value=None
        while not self.done.is_set():
            #self.cond.wait()
            self.cond.acquire()
            self.cond.wait()
            if self.queue:
                value=self.queue.pop(0)
                print("get%d"%value)
            self.cond.release()
            if value is None:
                self.misses+=1
            else:
                self.sum+=value
            #cond.release()
    
i=5
queue=[]
cond=Condition()

p=Producer(queue,cond,i)
c=Consumer(queue,cond)
c.start()
p.start()

time.sleep(1)
p.join()
with cond:
    cond.notify()
c.join()
print(c.sum,c.misses)

e=threading.Event()
e.is_set
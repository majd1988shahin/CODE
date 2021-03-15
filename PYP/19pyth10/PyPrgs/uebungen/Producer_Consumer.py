import threading,time, multiprocessing
from multiprocessing import Value
#from threading import Queue

class Producer(threading.Thread):
    def __init__(self,queue,qlock,howmany=5):
        self.queue=queue
        self.qlock=qlock
        self.howmany=howmany
        super().__init__()
    def run(self):
        for i in range(self.howmany):
            with self.qlock:
                self.queue.put(i)
            #time.sleep(0.05)
        print("Producer is done")

class Comsumer(threading.Thread):
    def __init__(self,queue,qlock):
        self.queue=queue
        self.qlock=qlock
        self.done=threading.Event()
        self.sum=0
        self.misses=0
        super().__init__()
    def join(self):
        self.done.set()
        super().join()
    def run(self):
        while not self.done.is_set():
            v=None
            time.sleep(0.1)
            with self.qlock:
                if self.queue:
                    v=self.queue.get()
            if v is not None:
                self.sum+=v
            else:
                self.misses+=1

q=multiprocessing.Queue()

qlock=threading.Lock()
p=Producer(q,qlock)
c=Comsumer(q,qlock)

p.start()
time.sleep(1)
c.start()

time.sleep(1)

p.join()
c.join()
print("sum=%d, misses=%d" % (c.sum, c.misses))
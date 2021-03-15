import threading,time, multiprocessing
from multiprocessing import Value


"""Safe counter DO NOT WORK"""
class T:
    def __init__(self):
        self.start=int(round(time.time() * 1000))
    def get(self):
        return int(round(time.time() * 1000))-self.start
    def reset(self):
        self.start=int(round(time.time() * 1000))

class counter:
    def __init__(self):
        self.val=0
    def inc(self):
        self.val+=1
    @property
    def value(self):
        return self.val

def run_counter(counter, times=1000000, incers=2):
    t=T()
    def incmany():
        for _ in range(times):
            counter.inc()
    threads = [threading.Thread(target=incmany)for _ in range(incers)]
    t.reset() 
    for thread in threads: # startall
        thread.start()

    for thread in threads: # joinall
        thread.join()
    class_name = counter.__class__.__name__
    value = counter.value
    used = t.get()
    print("%14s: %d, %s" % (class_name, value, used))


"""c=counter()
run_counter(c)"""

class safe_counter:
    def __init__(self):
        self.lock=threading.Lock()
        self.val=0

    def inc(self):
        self.lock.acquire()
        try:
            self.val+=1
        except:
            self.lock.release()
    @property
    def value(self):
        with self.lock:   
            return self.val
class Monetored_counter:
    def __init__(self):
        self.lock=threading.Lock()
        self.val=0

    def inc(self):
        with self.lock:
            self.val+=1
    @property
    def value(self):
        with self.lock:   
            return self.val
        

c=safe_counter()
m=Monetored_counter()
run_counter(m)

    
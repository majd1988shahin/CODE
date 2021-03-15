import threading,time
from threading import Event
e=threading.Event()
i=[]
e2=Event()
class w(threading.Thread):
  def __init__(self, e, i):
    self.e=e
    self.i=i
    self.stop=threading.Event()
    self.e.clear()
    super().__init__()
  def run(self):
    x=0
    while not self.stop.is_set():
      
      i.append(x)
      print("P ",len(i),x)
      time.sleep(0.1)
      x+=1

      self.e.set()
  def join(self):
    self.stop.set()
    super().join()
  
class r(threading.Thread):
  def __init__(self, e, i):
    self.e=e
    self.i=i
    self.stop=threading.Event()
    super().__init__()
  def run(self):
    
    while not self.stop.is_set():
      self.e.wait()
      print(i.pop(0))
      e.clear()
  def join(self):
    self.stop.set()
    super().join()

a=w(e,i)
b=r(e,i)

a.start()
b.start()

import time
time.sleep(1)
a.join()
b.join()


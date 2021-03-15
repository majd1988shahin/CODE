import threading,random, time
from random import random as rand

class Particle():
        def __init__(self,callback=None,speed=1/100, timestep=0.01,range_=(0.4,0.6)):
            self.x,self.y=rand(),rand()
            self.vx,self.vy=rand(),rand()
            self.speed=speed
            self.kannLauf=True
            self.pause_=True
            self.count=0
            self.callback=callback
            
            self.timestep=timestep
            super().__init__()
            self._stop_event = threading.Event()
            self.range_=range_
            self.th=threading.Thread(target=self.run)
            self.th.start()

        def get_position(self):#wir brauchen kein Lock , die Ergebnis ist sowieso Spalt !
            return self.x,self.y
                    
        def run(self):
            while self.kannLauf :
                time.sleep(self.timestep)
                if self.pause_:
                    continue
                else:
                    self.count+=1
                    self.vx,self.vy=(rand()-0.5)*self.speed,(rand()-0.5)*self.speed
                    self.x=self.x+self.vx 
                    self.y=self.y+self.vy
                    if self.x<self.range_[0]:self.x=self.range_[0]
                    if self.x>self.range_[1]:self.x=self.range_[1]
                    if self.y<self.range_[0]:self.y=self.range_[0]
                    if self.y>self.range_[1]:self.y=self.range_[1]
                    random.seed(self.count)
            
        def stop(self):
            self.kannLauf=False
            self.th.join()
            self._stop_event.set()
            
        
        def cont(self):
            self.pause_=False
        def pause(self):
            self.pause_=True
        def resume(self):
            self.pause_=False

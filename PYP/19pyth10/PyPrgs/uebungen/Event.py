from multiprocessing import Process
import os,time, threading


class Incer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.done=threading.Event()

    def run(self):
        x=0
        while not self.done.is_set():
            x+=1
            time.sleep(0.5)
            print("%d: x=%d"%(time.time(),x))
    
    def quit(self):
        self.done.set()
    def join(self):
        self.done.set()
        super().join()
    

inc=Incer()
inc.start()
time.sleep(2.3)
print("%d : quiting "%time.time())
#inc.quit()
time.sleep(0.2)
print("Allive ? %s" %inc.is_alive())
inc.join()
print("%dAllive ? %s" %(time.time(),inc.is_alive()))

import tkinter as tk
import time,threading,random,math
callbacks={"Re/start":lambda : print("Re/start"),
    "Pause":lambda : print("Pause"),
    "Quit" :lambda : print("Quit")}
class KeyPress:
    """KeyPress, instantiate and provide a frame to check in, most commonly
    use root. You can check anytime in the main thread, whether currently
    in the master a tracked key is pressed."""

    def __init__(self, master, keys):
        """bind the keypress events on the master widget.
        Provide the keys to track in a list keys.
        Assume that initially nothing is pressed"""
        master.bind_all('<KeyPress>', self._report_key_press)
        master.bind_all('<KeyRelease>', self._report_key_release)
        self.keys = dict()
        for key in keys:
            self.keys[key] = None # not pressed

    def _report_key_press(self, event):
        key = event.keysym
        if key in self.keys: # a tracked key
            self.keys[key] = time.time()

    def _report_key_release(self, event):
        key = event.keysym
        if key in self.keys: # a tracked key
            self.keys[key] = None

    def check(self, key):
        "find out whether a tracked key is pressed, use from main thread"
        return self.keys[key] is not None

    def pressed(self):
        "find out all currently pressed keys, use from main thread"
        return [key for key in self.keys if self.keys[key] is not None]

class Menu2(tk.Frame):
    def __init__(self,master=None,callbacks=callbacks):
        self.master=master
        super().__init__(master=self.master)
        self.callbacks=callbacks
        self.pack()
        
        self.btn_restart=tk.Button(master=self,text="Re/start")
        self.btn_restart.pack(side=tk.LEFT)
        self.btn_restart["command"]=self.restart
        self.btn_pause=tk.Button(master=self,text="Pause")
        self.btn_pause["command"]=self.Pause
        self.pause=False
        self.btn_pause.pack(side=tk.LEFT)
        tk.Button(master=self,text="Quit",command=self.callbacks["Quit"]).pack(side=tk.LEFT)
        self.lbl_score=tk.Label(master=self,text="00:00")
        self.lbl_score.pack()
        self.score=[0,0]
    def restart(self):
        self.callbacks["Re/start"]()
        self.score_update([0,0])
        self.btn_pause["text"]="Pause"
        self.pause=False

    def score_update(self,s):
        self.lbl_score["text"]="%02d:%02d"%(s[1],s[0])
        if 10 in s:
            self.Pause()
        self.score=s[:]
    def Pause(self):
        if 10 in self.score:
            return
        if self.pause==True:
            self.btn_pause["text"]="Pause"
            self.pause=False
        else:
            self.btn_pause["text"]="Resume"
            self.pause=True
        #print("Pause",self.pause)
        self.callbacks["Pause"](self.pause)

class drow(tk.Frame):
    def __init__(self,master=None,geometry="500x500"):
        self.master=master
        super().__init__(master)
        self.geometry=geometry
        self.pack()
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack(expand=True, fill=tk.BOTH,side=tk.BOTTOM)
        self.canvas["bg"] = "black"
    def update_poss(self,ball=[200,200],p1=0,p2=0):
        
        s=5
        self.canvas.delete("all")
        self.canvas.create_rectangle(ball[0]-s,ball[1]-s,ball[0]+s,ball[1]+s, fill="white")
        self.canvas.create_line(10,p1-15,10,p1+15,width=2,fill="white")
        self.canvas.create_line(390,p2-15,390,p2+15,width=2,fill="white")
        

class Game(tk.Frame):
    def __init__(self,master,FPS=25):
        super().__init__(master)
        self.master=master
        self.FPS=FPS
        callbacks["Re/start"]=self.Re_start
        callbacks["Pause"]=self.Pause
        callbacks["Quit"]=self.Quit
        self.menu=Menu2(master,callbacks=callbacks)
        self.drow=drow(master)
        self.ball=[200,200]
        self.v_ball=[0,0]
        self.p1=0
        self.p2=0
        self.score=[0,0]
        self.pause=False
        self.thread=None
        self.stop=threading.Event()
        keys = ["w","s","i","k"]
        self.keypress = KeyPress(self, keys)
        
    def Quit(self):
        if self.thread is not None:
            self.pause=True
            self.stop.set()
            self.thread.join()
        try:
            self.master.master.destroy()
        except:
            self.master.destroy()
    
    def Re_start(self):
        #print("Re/start")
        self.t=0
        self.score=[0,0]
        self.reset()

        self.pause=False
        if self.thread is None:
            self.stop=threading.Event()
            self.thread=threading.Thread(target=self.run)
            self.thread.start()
        return
    def Pause(self,status):
        self.pause=status

    def process_update(self):
        #print("in process")
        self.t=self.t+1
       
        c=self.keypress.pressed()
        #print(c)
        s=4
        v1=0
        v2=0
        if "w" in c     :v1=-s
        elif "s" in c   :v1= s
        if "i" in c     :v2=-s
        elif "k" in c   :v2= s
        
        self.p1+=v1
        self.p2+=v2
        if self.p1<15  :self.p1=15
        if self.p1>385 :self.p1=385
        if self.p2<15  :self.p2=15
        if self.p2>385 :self.p2=385

        ###############
        ##Ball#########
        if self.ball[1]>=400 or self.ball[1]<=0:self.v_ball[1]*=-1
        if 10<self.ball[0]<20:
            if self.p1-15<=self.ball[1]<=self.p1+15:
                self.v_ball[0]=int(math.fabs(self.v_ball[0]))
            else:
                self.set_score(1,0)
                self.reset()
        if 380<self.ball[0]<390:
            if self.p2-15<=self.ball[1]<=self.p2+15:
                self.v_ball[0]=-int(math.fabs(self.v_ball[0]))
            else:
                self.set_score(0,1)
                self.reset()
        self.ball[0]+=self.v_ball[0]
        self.ball[1]+=self.v_ball[1]
        return
    def set_score(self,a,b):
        self.score[0]+=a
        self.score[1]+=b
        self.menu.score_update(self.score)
    def reset(self):
        self.ball=[200,200]
        self.p1=200
        self.p2=200
        
        vx=random.randint(3,5)
        if random.random()<0.5:vx*=-1
        vy=random.randint(2,4)
        if random.random()<0.5:vy*=-1
        self.v_ball=[vx,vy]

    def run(self):
        while not self.stop.is_set():
            time.sleep(1/self.FPS)
            if not self.pause:
                self.process_update()
                #print(self.p1)
                self.drow.update_poss(self.ball,self.p1,self.p2)



root=tk.Tk()
root.title("TkPong")

game=Game(root,FPS=25)

root.mainloop()
    

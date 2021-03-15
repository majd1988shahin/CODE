import tkinter as tk
class Greeting:
    def __init__(self):
        self.G=["Hallo","Hi","Aloita","Oi"]
        self.i=0
    def get_next_greeting(self):
        self.i=(self.i+1)%len(self.G)
        return self.G[self.i]

class Main(tk.Frame):
    def __init__(self,root):
        tk.Frame.__init__(self,root)
        self.Greeting=Greeting()
        self.creatWidgets()
        self.pack(expand=True,fill=tk.BOTH)
        
    def callback(self):
        self.lable["text"]=self.Greeting.get_next_greeting()
        
    def creatWidgets(self):
        self.lable=tk.Label(self,text="Hallo")
        self.lable.pack()
        frame=tk.Frame(self)
        frame.pack()
        gruss=tk.Button(frame,text="Grüße",command=self.callback)
        gruss.pack(side=tk.LEFT)
        beende=tk.Button(frame,text="Beenden",command=self._root().destroy)
        beende["fg"]="red"
        beende.pack(side=tk.LEFT)


if __name__=="__main__":
    root=tk.Tk()
    main=Main(root)
    root.mainloop()
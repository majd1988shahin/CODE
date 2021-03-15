import tkinter as tk
import time
class Root(tk.Tk):
    def __init__(self,callback,infos2):
        super().__init__()
        self.callback=callback
        self.creatwigets()
        self.infos2=infos2
        
    def creatwigets(self):
        self.txt=tk.Text(self)
        self.txt.pack()

    def destroy(self):
        infos=self.txt.get("1.0","end-1c")
        self.callback(infos)
        self.infos2["text"]=infos
        super().destroy()
    

if __name__=="__main__":
    infos=""
    def callback(infos_):
        global infos
        infos=infos_
    infos2={}
    root=Root(callback,infos2)
    root.mainloop()
    print(infos,infos2)
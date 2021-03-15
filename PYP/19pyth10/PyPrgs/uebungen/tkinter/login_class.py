import tkinter as tk 

class Login(tk.Frame):
    def __init__(self,master=None,callback=None):
        tk.Frame.__init__(self,master)
        tk.Label(self,text="Benutzer").grid(row=0,column=0)
        tk.Label(self,text="Passwort").grid(row=1,column=0)

        self.userEntry=tk.Entry(self,width=17)
        self.passwortEntry=tk.Entry(self,width=17,show="*")
        self.userEntry.grid(row=0,column=1)
        self.passwortEntry.grid(row=1,column=1)

        buttonFrame=tk.Frame(self)
        buttonFrame.grid(row=2,column=0,columnspan=2)
        tk.Button(buttonFrame,text="OK",
            command=lambda : callback(True,self.userEntry.get(),self.passwortEntry.get())).pack(side=tk.LEFT)
        tk.Button(buttonFrame,text="Löschen",
            command=lambda:
                (self.userEntry.delete(0,tk.END),self.passwortEntry.delete(0,tk.END))).pack(side=tk.LEFT)
        tk.Button(buttonFrame,text="Abbrechen",
            command=lambda:callback(False,None,None)).pack(side=tk.LEFT)
        
        
def callback(state,user,password):
    print(state,user,password)
    root.destroy()
    
root=tk.Tk()
login=Login(root,callback)
login.pack()
root.mainloop()


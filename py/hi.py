import tkinter as tk 
import pickle

class Menu1(tk.Frame):
    "Main Menu für tkChat App"
    def __init__(self,master=None,callback=None):
        tk.Frame.__init__(self,master)
        ##wir versuchen, die Informationen zu lesen
        try:
            of=open("infos.pickle","rb")
            self.infos=pickle.load(of)
        ##Sonst benuzen wir Defult Informationen
        except:
            self.infos={"User_Name":"None","Auto_Update":False,"Auto_update_interval":None}

        ##Main Menu Buttons
        tk.Button(self,text="Refresh",command=self.f_refresh).pack(side=tk.LEFT)
        tk.Button(self,text="Settings",command=self.f_setting).pack(side=tk.LEFT)
        tk.Button(self,text="Quit",command=self.f_quit).pack(side=tk.LEFT)
        self.master=master
        self.pack(side=tk.LEFT,anchor=tk.NW,fill=tk.X,expand=True)


    def f_refresh(self):
        "refresh Fenster "
        #implementiere etwas hier !!
        print("Refreshing")

    def update_infos(self,infos):
        "Update Informationen über user-name / Updates interval"
        #implementiere etwas hier !!

        #die Informationen werden da gespeichert werden
        pickle.dump(infos,open("infos.pickle","wb"))
        print("Du bekommst Informationen")
        self.infos=infos
        print(self.infos)
    

    def f_quit(self):
        "Fenster schliesen"
        #implementiere etwas hier !! um die App zu beenden
        
        print("Quit")
        self.master.destroy()

    def f_setting(self):
        print("Setting Window is called")
        s=self.Setting(infos=self.infos,callback=self.update_infos)
        s.title="setting"
    
    class Setting:
        def __init__(self,callback=None,infos=None):
            "Setting Fenster"
            self.callback=callback
            self.top=tk.Tk()
            self.top.title("Setting")
            #Labels 
            tk.Label(self.top,text="Kürzel").grid(row=0,column=0)
            tk.Label(self.top,text="Auto-Update").grid(row=1,column=0)
            tk.Label(self.top,text="Auto-Update-Interval").grid(row=2,column=0)

            #User-Name Entry
            self.en_user_name=tk.Entry(self.top,width=12)
            self.en_user_name.grid(row=0,column=1)

            #Auto-Update Checkbutton & Boolean Variable
            self.v_auto_update=tk.BooleanVar(self.top)
            self.cb_auto_update=tk.Checkbutton(self.top,variable=self.v_auto_update,
                command=self.toggle_auto_update_interval)
            self.cb_auto_update.grid(row=1,column=1)
            
            #Auto Update Interval
            self.en_auto_update_interval=tk.Entry(self.top,width=12,state="disabled")
            self.en_auto_update_interval.grid(row=2,column=1)

            #Wir Schreiben die Alte Informationen auf Entries & CheckBox
            self.infos=infos
            self.en_user_name.insert(0,self.infos["User_Name"])
            if self.infos["Auto_Update"]:
                self.cb_auto_update.select();self.toggle_auto_update_interval()
                self.en_auto_update_interval.insert(0,"%3.3f"%self.infos["Auto_update_interval"])
                
            #OK & Cancel Buttom um das Fenster der Eigenschaften zu schliesen 
            # und die Informationen zurückzugeben
            tk.Button(self.top,text="Cancel",command=self.cancel).grid(row=3,column=0,sticky=tk.E)
            tk.Button(self.top,text="OK",command=self.ok).grid(row=3,column=1,sticky=tk.W)
            
        def toggle_auto_update_interval(self):
            if self.v_auto_update.get():
                self.en_auto_update_interval.config(state="normal")
            else:
                self.en_auto_update_interval.config(state="disable")

        def cancel(self):
            "Schliest das Fenster und liefert die Alte Informationen"
            self.callback(self.infos)
            self.top.destroy()

        def ok(self):
            "Schliest das Fenster und liefert die Neue Informationen"

            #wir sammlen die neue Informationen
            self.infos["User_Name"]=self.en_user_name.get()
            self.infos["Auto_Update"]=self.v_auto_update.get()
            if self.v_auto_update.get():
                self.infos["Auto_update_interval"]=float(self.en_auto_update_interval.get()) 
            else :
                self.infos["Auto_update_interval"]=None
            
            #und wir senden sie zurück
            self.callback(self.infos)
            self.top.destroy()

#An Example for implement Menu1 class   
      
root=tk.Tk()
root.title("tkChat")
root.geometry("600x300")
menu=Menu1(root)


root.mainloop()

import tkinter as tk 

root= tk.Tk()

text=tk.Text(root,height=3,width =12)
text.pack()
tk.Button(root,text="show",command=lambda :print(text.get(1.0,tk.END))).pack()

f1=tk.Frame(root,width=100,height=100,bg="black")
f1.pack()
f2=tk.Frame(f1,width=20,height=20,bg="white")
f2.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
var2=tk.IntVar()
sc=tk.Scale(root,from_=0, to=255,variable=var2,orient=tk.HORIZONTAL)
sc.pack()
sc2=tk.Scale(root,from_=0, to=255,variable=var2,orient=tk.HORIZONTAL)
sc2.pack()
def update(*args):
    #print(args)
    f2["bg"]="#"+("%02x"%var2.get())*3
sc["command"]=update
var2.trace("w",update)
#sc.set(255)
root.mainloop()
import tkinter as tk 

root= tk.Tk()


lb=tk.Listbox(root,height=4,width=20)
lb.pack()
entries=["Mein", "Name", "ist", "Majd"]
for e in entries:
    lb.insert(-1,e)
tk.Button(root,text="Show",command=lambda : print(lb.curselection())).pack(side=tk.LEFT)
def togle_mode():
    if lb["selectmode"]==tk.BROWSE:
        lb["selectmode"]=tk.EXTENDED
    else:lb["selectmode"]=tk.BROWSE
tk.Button(root,text="Mode",command=togle_mode).pack(side=tk.LEFT)

root.mainloop()


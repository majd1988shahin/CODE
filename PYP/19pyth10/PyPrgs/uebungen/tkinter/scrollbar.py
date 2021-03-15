import tkinter as tk

root=tk.Tk()
sb=tk.Scrollbar(root)
sb.pack(side=tk.RIGHT,fill=tk.Y)#Scrollbar ist nur der klein link Teil !! verbunden mit Listbox
lb=tk.Listbox(root,yscrollcommand=sb.set)
for i in range(100):
    lb.insert(tk.END,"N %d"%i)

lb.pack()
sb.config(command=lb.yview)

root.mainloop()
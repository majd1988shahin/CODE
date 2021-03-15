import tkinter as tk

root=tk.Tk()
bvar=tk.BooleanVar()
def f1():
    print(bvar.get())
cb=tk.Checkbutton(root,text="An/Aus",variable=bvar,command=lambda:print(bvar.get()))
btn=tk.Button(root,text="toggle checkbox",command=lambda:(cb.toggle(),print(bvar.get())))

cb.pack()
btn.pack()

root.mainloop()
del root
##################
root=tk.Tk()
entry=tk.Entry(root,bg="white")
entry.pack()

tk.Button(root,text="delet",command=lambda:(print(entry.get()),entry.delete(0,tk.END))).pack()
tk.Button(root,text="reset",command=lambda:(entry.delete(0,tk.END),entry.insert(0,"Vorgabe"))).pack()

root.mainloop()
import tkinter as tk 

root=tk.Tk()
names=["Graham", "Eric", "TerryG", "TerryJ","John", "Michael"]
radios,var=[],tk.IntVar()

for idx, name in enumerate(names):
    radio=tk.Radiobutton(root,text=name,variable=var,value=idx)
    radios.append(radio)
    

var.set(0)
lbl=tk.Label(root,text=names[var.get()])
lbl.pack()
def f():
    lbl["text"]=names[var.get()]
    #print(var.get())
for radio in radios:
    #radio["command"]= f
    radio.pack(anchor=tk.W)

def update(*args):
    lbl["text"] = names[var.get()]
    print(var.get())
var.trace("w", update) # follow changes
tk.Button(root,text="Next",command=lambda:var.set((var.get()+1)%len(names))).pack()
root.mainloop()

var = tk.IntVar()
def tracer(*args):
    print("trace: %d" % var.get())
var.set(17)
tracename = var.trace("w", tracer)
var.set(42) # trace: 42

print(var.trace_vinfo())
#[(’w’, ’140256148065488tracer’)] 
var.trace_vdelete("w", tracename)

var.set(69)
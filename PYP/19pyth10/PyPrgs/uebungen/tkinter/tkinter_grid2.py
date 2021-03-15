import tkinter as tk

root =tk.Tk()
frame=tk.Frame(root)

labels=[tk.Label(frame,bg="red",text="lable{0}{1}".format(i,j)) for i in range(0,4) for j in range(0,4)]
for i in range(4):
    for j in range(4):
        labels[i*4+j].grid(row=i,column=j,sticky=tk.NSEW)
for i in range(4):
    frame.columnconfigure(i,weight=1)
    frame.rowconfigure(i,weight=1)
frame.pack(expand=True,fill=tk.BOTH)
root.mainloop()
        

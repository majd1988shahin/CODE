import tkinter as tk

root=tk.Tk()
root.minsize(320, 120)
frames = [tk.Frame(root, bg="red") for i in range(5)]
for i in range(5):
        frames[i].pack(fill=tk.BOTH, expand=True)
labels = [tk.Label(frames[i//3],bg="lightgreen", relief=tk.SUNKEN,
                text="Label%02d"%i) for i in range(15)]
for i in range(5):
    for j in range(3):
        labels[i*3+j].grid(row=i, column=j,sticky=tk.EW,)
frames[1].columnconfigure(0, weight=1)
frames[2].columnconfigure(2, weight=1)
frames[2].columnconfigure(1, weight=1)
frames[3].columnconfigure(0, weight=1)
frames[3].columnconfigure(1, weight=2)
frames[4].columnconfigure(0, weight=1)
frames[4].columnconfigure(1, weight=2)
frames[4].columnconfigure(2, weight=4)
for i in range(5):
        for j in range(3):
             frames[i].columnconfigure(j, weight=1)   

root.mainloop()
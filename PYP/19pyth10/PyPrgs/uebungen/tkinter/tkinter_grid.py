import tkinter as tk

def main(root):
    labels=[tk.Label(root,bg="lightgreen",text="Lebel%d"%i ) for i in range(14)]
    for i in range(3):
        labels[i].grid(row=0,column=i)
    labels[3].grid(row=1,column=0)
    labels[4].grid(row=1,column=2)
    labels[5].grid(row=2,column=0,columnspan=3)
    labels[6].grid(row=3,column=2,columnspan=3,sticky=tk.E,pady=6,ipadx=17)
    labels[7].grid(row=4,column=0,sticky=tk.W)
    labels[8].grid(row=5,column=0,columnspan=3,sticky=tk.E+tk.W)
    for i in range(4):
        labels[9+i].grid(row=i+6,column=0)
    labels[13].grid(column=2,row=6,rowspan=4,sticky=tk.NS)

if __name__=="__main__":
    root=tk.Tk()
    main(root)
    root.mainloop()
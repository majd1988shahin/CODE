import tkinter as tk

def main(root):
    labels=[tk.Label(root,bg="lightgreen",text="Lebel%d"%i ) for i in range(8)]
    labels[0].pack(expand=True)
    labels[1].pack(fill=tk.X,expand=True)
    labels[2].pack(fill=tk.X,padx=3,pady=3,expand=True)
    labels[3].pack(fill=tk.X,ipady=15,expand=True)
    labels[4].pack(side=tk.LEFT,expand=True)
    labels[5].pack(side=tk.RIGHT,fill=tk.Y,expand=True)
    labels[6].pack(expand=True)
    labels[7].pack(expand=True)


if __name__=="__main__":
    root=tk.Tk()
    main(root)
    root.mainloop()
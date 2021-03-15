import tkinter as tk
GREETING=["Hallo","Hi","Aloita","Oi"]
IDX=0
def callback():
    global IDX
    IDX=(IDX+1)%len(GREETING)
    lable["text"]=GREETING[IDX]
def main(root):
    global lable
    lable=tk.Label(root,text=GREETING[IDX])
    lable.pack()
    frame=tk.Frame(root)
    frame.pack()
    gruss=tk.Button(frame,text="Grüße",command=callback)
    gruss.pack(side=tk.LEFT)
    beende=tk.Button(frame,text="Beende",command=root.destroy)
    beende["fg"]="red"
    beende.pack(side=tk.LEFT)
    



if __name__=="__main__":
    root=tk.Tk()
    main(root)
    root.mainloop()
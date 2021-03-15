import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()
def s(root):
    root.minsize(320, 120)
    label = tk.Label(root, text="Ein Label")
    label["bg"] = "lightgreen"
    label["fg"] = "gray17"
    label["font"] = "Arial 20" 
    label.pack()
    
    img = Image.open('a.jpg')
    img = img.resize((300,200), Image.ANTIALIAS)
    
    photo = ImageTk.PhotoImage(img)
    imLable=tk.Label(root,image=photo)
    imLable.photo=photo ## wechtig !!
    imLable.pack()

s(root)   
root.mainloop()
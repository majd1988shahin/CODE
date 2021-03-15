import tkinter as tk

root=tk.Tk()

btn=tk.Button(root,text="Druecke mich")
btn["font"]="Arial 20"
btn["bg"]="green"
btn["fg"]="gray17"
btn["disabledforeground"]="gray50"
btn["highlightbackground"]="yellow"
btn["highlightcolor"]="purple"
btn["activebackground"]="magenta"

btn["command"]=lambda : (print("klicked"),btn.update())
btn.pack()

def f():
    if btn["state"]=="normal":btn["state"]="disabled"
    else:btn["state"]="normal"
btn_toggle=tk.Button(root, text="Toggle State")
btn_toggle["command"]=f
btn_toggle.pack()

root.mainloop()
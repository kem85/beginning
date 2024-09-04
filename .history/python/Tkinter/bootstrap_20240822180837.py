import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *

root = tb.Window(themename="vapor")
relx = 0.3
rely = 0.1
text_var = tk.StringVar()
lst = ["gorilla","moshella","mushella","mosheila","garilla","boot","broooot","league","of","grame","abooo","league"]
def on_text_change(*args):
    index = 0
    curt = text_var.get()
    nlst = [word[:-(len(word)-len(curt))] if len(word) > len(curt) else word for word in lst]
    for i,cur in enumerate(nlst):
        if cur.lower() == curt.lower() and len(curt)!=0:
            print(lst[i])
def subsub():
    global relx, rely
    rely += 0.1
    button1 = tb.Button(text="great", style="PRIMARY",takefocus=False)
    button1.place(relx=relx, rely=rely)

root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 400
windowHeight = 400
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(False, False)
#Main Frame

button = tb.Button(root, text="what is love", style="PRIMARY", command=subsub, takefocus=False)
button.place(relx=0.5, rely=0.1, anchor='ne')
search = tb.Entry(root, textvariable=text_var,width="30")
search.pack(padx=10, pady=10)
text_var.trace_add("write", on_text_change)
root.mainloop()

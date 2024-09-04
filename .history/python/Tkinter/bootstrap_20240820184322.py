import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
from tkinter import *
root = tb.Window(themename="vapor")
def subsub():
    print(relx.get(),rely.get())
    button1 = tb.Button(text="great",style="PRIMARY")
    button1.place(relx = relx.get(), 
                  rely = rely.get())
root.title("Accounts")
relx = tb.IntVar()
rely=  tb.IntVar()
root.iconbitmap('skills.ico')
windowWidth = 400
windowHeight = 400
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(False,False)
relx.set()
button = tb.Button(root,text="what is love",style="PRIMARY",command= lambda:subsub(),takefocus=False)
button.place(relx = 0.5, 
                  rely = 0.1,
                  anchor ='ne')
root.mainloop()
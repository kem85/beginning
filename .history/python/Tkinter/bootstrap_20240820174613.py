import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
from tkinter import *
root = tb.Window(themename="vapor")
def subsub():
    print("love is great")
root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 400
windowHeight = 400
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(False,False)
button = tb.Button(root,text="what is love",style="PRIMARY",command=lambda: subsub(),takefocus=False)
button.place(relx=1.0,
             rely=0)
button.pack(padx=10,pady=10)
root.mainloop()
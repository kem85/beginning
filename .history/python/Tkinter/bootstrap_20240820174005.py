import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
from tkinter import *
root = tb.Window(themename="vapor")
root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 400
windowHeight = 400
root.eval('tk::PlaceWindow . center')
root.resizable(False,False)
button = tb.Button(root,text="what is love",style="PRIMARY")
button.pack(padx=10,pady=10)
root.mainloop()
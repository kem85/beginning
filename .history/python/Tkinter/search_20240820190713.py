import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
root = tb.Window(themename="vapor")
root.title("Search")
count = 0
current = ""
def on_text_change(event):
    global count
    if count == 0:
        current = search.get()
        count+= 1
    else:
        count--
    current_text = search.get()
    print("Text changed:", current_text)
root.iconbitmap('skills.ico')
windowWidth = 400
windowHeight = 400
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(False, False)
search = tb.Entry(root)
search.pack(padx=10, pady=10)
search.bind("<KeyRelease>", on_text_change)
root.mainloop()
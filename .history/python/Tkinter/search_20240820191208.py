import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
root = tb.Window(themename="vapor")
root.title("Search")
text_var = tk.StringVar()
def on_text_change(*args):
    current_text = text_var.get()
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
text_box = tk.Entry(root, textvariable=text_var)
text_box.pack(padx=10, pady=10)

# Trace changes in the StringVar
text_var.trace_add("write", on_text_change)
root.mainloop()
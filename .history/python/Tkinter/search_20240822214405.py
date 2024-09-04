import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
from tkinter import *

root = tb.Window(themename="vapor")
text_var = tk.StringVar()
lst = ["gorilla","moshella","mushella","mosheila","garilla","boot","broooot","league","of","grame","abooo","league"]
def on_text_change(*args):
    index = 0
    curt = text_var.get()
    nlst = [word[:-(len(word)-len(curt))] if len(word) > len(curt) else word for word in lst]
    for i,cur in enumerate(nlst):
        if cur.lower() == curt.lower() and len(curt)!=0:
            print(lst[i])
def on_mousewheel(event):
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def update_scrollregion():
    my_canvas.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))
root.title("Debugging Example")
windowWidth = 450
windowHeight = 550
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(False, False)
# Main Frame
main_frame = tb.Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Canvas
my_canvas = tb.Canvas(main_frame, bg="white", width=300, height=500)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Scrollbar for the canvas
my_scrollbar = tb.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)

# Create a frame inside the canvas
second_frame = Frame(my_canvas, bg="lightgrey", width=300, height=50*30)  # Ensure it's large enough
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Add some buttons to the frame
for i in range(50):
    button = tb.Button(second_frame, text=f'Button {i}', width=15)
    button.place(x=100, y=i * 30,anchor=tb.CENTER)  # Adjust the `y` coordinate for vertical placement

search = tb.Entry(root, textvariable=text_var,width=30)
search.pack(padx=10, pady=10)
# Update scroll region to include all buttons
update_scrollregion()

# Bind mouse wheel scrolling
root.bind_all("<MouseWheel>", on_mousewheel)
text_var.trace_add("write", on_text_change)
root.mainloop()

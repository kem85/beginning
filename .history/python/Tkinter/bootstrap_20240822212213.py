import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *

root = tb.Window(themename="vapor")

def on_mousewheel(event):
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

root.title("Simple Example")
root.iconbitmap('skills.ico')
windowWidth = 400
windowHeight = 600
root.geometry(f'{windowWidth}x{windowHeight}')

# Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Canvas
my_canvas = Canvas(main_frame, bg="white")
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Scrollbar for the canvas
my_scrollbar = tb.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)

# Create a frame inside the canvas
second_frame = Frame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Add a few buttons to the frame
for i in range(10):
    button = tb.Button(second_frame, text=f'Button {i}', takefocus=False, width=15, style="PRIMARY")
    button.place(x=10, y=i * 30)

# Update scroll region to include all buttons
def update_scrollregion():
    my_canvas.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

update_scrollregion()

# Bind mouse wheel scrolling
root.bind_all("<MouseWheel>", on_mousewheel)

root.mainloop()

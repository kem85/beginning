import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
from tkinter import *
def on_mousewheel(event):
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def update_scrollregion():
    my_canvas.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

root = tb.Window(themename="vapor")
root.title("Debugging Example")
root.geometry('400x600')

# Main Frame
main_frame = tk.Frame(root, bg="lightblue")
main_frame.pack(fill=tk.BOTH, expand=1)

# Canvas
my_canvas = tk.Canvas(main_frame, bg="white", width=300, height=500)
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Scrollbar for the canvas
my_scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)

# Create a frame inside the canvas
second_frame = tk.Frame(my_canvas, bg="lightgrey", width=300, height=1500)  # Ensure it's large enough
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Add some buttons to the frame
for i in range(50):
    button = tk.Button(second_frame, text=f'Button {i}', width=15)
    button.place(x=10, y=i * 30)  # Adjust the `y` coordinate for vertical placement

# Update scroll region to include all buttons
update_scrollregion()

# Bind mouse wheel scrolling
root.bind_all("<MouseWheel>", on_mousewheel)

root.mainloop()

import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *

root = tb.Window(themename="vapor")
text_var = tk.StringVar()
lst = ["gorilla", "moshella", "mushella", "mosheila", "garilla", "boot", "broooot", "league", "of", "grame", "abooo", "league"]

def on_text_change(*args):
    curt = text_var.get()
    nlst = [word[:-(len(word)-len(curt))] if len(word) > len(curt) else word for word in lst]
    for i, cur in enumerate(nlst):
        if cur.lower() == curt.lower() and len(curt) != 0:
            print(lst[i])

def on_mousewheel(event):
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def update_scrollregion():
    my_canvas.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

root.title("Debugging Example")
windowWidth = 400
windowHeight = 400  # Fixed height
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth / 2 - windowWidth / 2)
centerY = int(screenHeight / 2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(True, True)  # Allow resizing

# Main Frame
main_frame = tb.Frame(root)
main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Canvas
my_canvas = tb.Canvas(main_frame, bg="white")
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Scrollbar for the Canvas
my_scrollbar = tb.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)

# Frame inside the Canvas
second_frame = tk.Frame(my_canvas, bg="lightgrey", width=windowWidth - 20, height=50*30)  # Width adjusted to canvas size
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Add Buttons to the Frame
for i in range(50):
    button = tk.Button(second_frame, text=f'Button {i}', width=15)
    button.place(x=10, y=i * 30)  # Adjust the `y` coordinate for vertical placement

# Bottom Frame for the Search Entry
bottom_frame = tb.Frame(root, height=30)  # Fixed height for bottom frame
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

search = tb.Entry(bottom_frame, textvariable=text_var, width=30)
search.pack(padx=10, pady=10)

# Adjust Canvas height based on the window height and the height of the bottom frame
canvas_height = windowHeight - bottom_frame.winfo_height()
my_canvas.config(height=canvas_height)

# Update Scroll Region
update_scrollregion()

# Bind Mouse Wheel Scrolling
root.bind_all("<MouseWheel>", on_mousewheel)

text_var.trace_add("write", on_text_change)
root.mainloop()

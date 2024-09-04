import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *

root = tb.Window(themename="vapor")
text_var = tk.StringVar()

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

root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 400
windowHeight = 800  # Increase height to accommodate more buttons
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth / 2 - windowWidth / 2)
centerY = int(screenHeight / 2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(True, True)

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

# Create second frame inside the canvas
second_frame = Frame(my_canvas, b="lightgrey")
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Add buttons to the frame
for i in range(50):
    button = tb.Button(second_frame, text=f'Pablo {i}', takefocus=False, width=15, style="PRIMARY")
    button.place(x=10, y=i * 30)  # Adjust the `y` coordinate for vertical placement
    print(f'Button {i} placed at y={i * 30}')  # Debug output to confirm button placement

# Update scroll region to include all buttons
update_scrollregion()

# Entry widget
search = tb.Entry(root, textvariable=text_var, width="30")
search.pack(padx=10, pady=10)

text_var.trace_add("write", on_text_change)

root.bind_all("<MouseWheel>", on_mousewheel)

root.mainloop()

import tkinter as tk
import ttkbootstrap as tb
from tkinter import Frame, VERTICAL, Y

# Set up the main window
root = tb.Window(themename="vapor")

# Function to handle mouse wheel scrolling
def on_mousewheel(event):
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Function to update the scroll region
def update_scrollregion():
    my_canvas.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

# Set up the main window dimensions
windowWidth = 340
windowHeight = 450
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth / 2 - windowWidth / 2)
centerY = int(screenHeight / 2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(False, False)

# Create the main frame and canvas
main_frame = tb.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

my_canvas = tb.Canvas(main_frame, width=100, height=405, bg='#110833')
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Add a scrollbar to the canvas
my_scrollbar = tb.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=Y)

# Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind_all("<MouseWheel>", on_mousewheel)

# Create a second frame inside the canvas
second_frame = Frame(my_canvas, width=340, bg='#110833')
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Generate a lot of buttons to test scrolling
for i in range(10):
    button = tb.Button(second_frame, text=f'Button {i}', takefocus=False, width=20)
    button.pack(pady=5, padx=10, anchor='w')

# Initialize scroll region
update_scrollregion()

# Start the main event loop
root.mainloop()

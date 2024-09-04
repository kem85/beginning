import tkinter as tk
import ttkbootstrap as tb
from tkinter import Frame, VERTICAL, Y

# Set up the main window
root = tb.Window(themename="vapor")

# Function to handle mouse wheel scrolling
def on_mousewheel(event):
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Function to update the scroll region with a minimum height
def update_scrollregion():
    min_height = 405  # Adjust this value as needed
    my_canvas.update_idletasks()
    bbox = my_canvas.bbox("all")
    my_canvas.configure(scrollregion=(bbox[0], bbox[1], bbox[2], max(bbox[3], min_height)))

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

my_canvas = tb.Canvas(main_frame, bg='#110833')
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Add a scrollbar to the canvas
my_scrollbar = tb.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=Y)

# Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind("<MouseWheel>", on_mousewheel)

# Create a second frame inside the canvas
second_frame = Frame(my_canvas, width=windowWidth, bg='#110833')
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Generate a number of buttons to test scrolling
for i in range(1):  # Test with fewer buttons, e.g., 10
    button = tb.Button(second_frame, text=f'Button {i}', takefocus=False, width=20)
    button.pack(pady=5, padx=10, anchor='w')

# Update scroll region after all buttons are packed
update_scrollregion()

# Start the main event loop
root.mainloop()

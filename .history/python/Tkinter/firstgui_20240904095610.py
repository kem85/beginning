import tkinter as tk
import ttkbootstrap as tb
from tkinter import Frame, VERTICAL, Y

# Set up the main window
root = tb.Window(themename="vapor")

# Function to handle mouse wheel scrolling
def on_mousewheel(event):
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Function to update the scroll region with a minimum height
def update_scrollregion():import tkinter as tk
import ttkbootstrap as tb
from tkinter import Frame, VERTICAL, Y

# Set up the main window
root = tb.Window(themename="vapor")

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

# Create a second frame inside the canvas
second_frame = Frame(my_canvas, bg='#110833')
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Function to handle updating or creating buttons
def update_buttons(indic, update):
    if indic == 'category':
        if not update:
            for i in range(45):  # Example: create 45 buttons
                button = tb.Button(second_frame, text=f'Button {i}', takefocus=False, width=13, style='Custom.TButton')
                if i % 2 == 0:
                    button.place(x=7, y=i*35)
                else:
                    button.place(x=180, y=(i-1)*35)
        else:
            # Example: update button positions
            pos = poscat_var.get()
            if pos < len(buttons):
                button = buttons[pos]
                button.place_forget()  # Remove the old placement
                button = tb.Button(second_frame, text=f'Button {pos}', takefocus=False, width=13, style='Custom.TButton')
                if pos % 2 == 0:
                    button.place(x=7, y=pos*35)
                else:
                    button.place(x=180, y=(pos-1)*35)
                buttons[pos] = button
            else:
                button = tb.Button(second_frame, text=f'Button {pos}', takefocus=False, width=13, style='Custom.TButton')
                if pos % 2 == 0:
                    button.place(x=7, y=pos*35)
                else:
                    button.place(x=180, y=(pos-1)*35)
                buttons.append(button)
            poscat_var.set(poscat_var.get() + 1)
        # Update the scroll region
        update_scrollregion()

# Initialize the list to keep track of buttons
buttons = []

# Create and update a few buttons for testing
poscat_var = tk.IntVar(value=0)
update_buttons('category', False)
update_buttons('category', True)

# Update scroll region function
def update_scrollregion():
    my_canvas.update_idletasks()
    bbox = my_canvas.bbox("all")
    if bbox:
        my_canvas.configure(scrollregion=bbox)

# Start the main event loop
root.mainloop()

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
for i in range(10):  # Test with fewer buttons, e.g., 10
    button = tb.Button(second_frame, text=f'Button {i}', takefocus=False, width=20)
    button.pack(pady=5, padx=10, anchor='w')

# Update scroll region after all buttons are packed
update_scrollregion()

# Start the main event loop
root.mainloop()

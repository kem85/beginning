import tkinter as tk
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

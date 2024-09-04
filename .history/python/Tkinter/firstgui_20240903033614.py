import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

# Create the main window
root = tk.Tk()
root.title("Combobox Font Size Example")

# Define options for the combobox
options = ["Option 1", "Option 2", "Option 3"]

# Create the combobox
combobox = ttk.Combobox(root, values=options)
combobox.pack(pady=20)

# Configure the font for the dropdown menu
def configure_font(event):
    # Access the internal Listbox used for the dropdown menu
    listbox = combobox.tk.call(combobox._w, 'noconflict', 'listbox')
    listbox_font = tkfont.Font(family="Helvetica", size=12)  # Customize font size here
    combobox.tk.call(listbox, 'configure', '-font', listbox_font.actual())

# Use the event when the combobox is clicked
combobox.bind('<Button-1>', configure_font)

# Run the Tkinter event loop
root.mainloop()

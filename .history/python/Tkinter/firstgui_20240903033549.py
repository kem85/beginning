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

# Access the internal Listbox used for the dropdown menu
def configure_font(event):
    # Access the Listbox widget and configure its font
    listbox = combobox.tk.call(combobox._w, 'noconflict', 'listbox')
    listbox_font = tkfont.Font(family="Helvetica", size=50)  # Customize font size here
    combobox.tk.call(listbox, 'configure', '-font', listbox_font.actual())

# Bind to the <Map> event, which is triggered when the widget is displayed
combobox.bind('<Map>', configure_font)

# Run the Tkinter event loop
root.mainloop()

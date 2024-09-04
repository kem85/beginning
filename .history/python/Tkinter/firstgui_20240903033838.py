import tkinter as tk
import ttkbootstrap as ttk
from tkinter import StringVar

# Create the main application window
root = ttk.Window(themename='darkly')

# Adjust the font for the Combobox dropdown menu
root.option_add('*TCombobox*Listbox.font', ('Arial', 14))  # Change font size here

# Create a Combobox
var = StringVar()
combo = ttk.Combobox(root, textvariable=var, font=('Arial', 14))  # Adjust font for entry part as well
combo['values'] = ("Option 1", "Option 2", "Option 3")
combo.pack(pady=20)

# Run the application
root.mainloop()

import tkinter as tk
import ttkbootstrap as ttk
from tkinter import StringVar

# Create the main application window
root = ttk.Window(themename='darkly')

# Create a style object
style = ttk.Style()

# Customize the font size of the Combobox menu
style.configure('TCombobox', font=('Arial', 14))  # Increase the font size here

# Create a Combobox
var = StringVar()
combo = ttk.Combobox(root, textvariable=var, style='TCombobox')
combo['values'] = ("Option 1", "Option 2", "Option 3")
combo.pack(pady=20)

# Run the application
root.mainloop()

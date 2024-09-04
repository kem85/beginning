import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

class CustomCombobox(ttk.Combobox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self._set_dropdown_font()
        
    def _set_dropdown_font(self):
        # Create a font object with the desired size
        font = tkfont.Font(family="Helvetica", size=12)
        
        # Update the internal listbox font (works for most Tkinter versions)
        self.bind('<Map>', lambda e: self._apply_font(font))
    
    def _apply_font(self, font):
        # Access the internal Listbox and set its font
        self.tk.call(self._w + "_popup", "configure", "-font", font.actual())

# Create the main window
root = tk.Tk()
root.title("Custom Combobox Font Size Example")

# Define options for the combobox
options = ["Option 1", "Option 2", "Option 3"]

# Create the custom combobox
combobox = CustomCombobox(root, values=options)
combobox.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

import tkinter as tk
import ctypes
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.geometry("400x300")
root.title("Custom Title Bar Color")

# Function to change the title bar color (Windows 10+ only)
def set_window_title_bar_color(color_hex):
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 35, ctypes.byref(ctypes.c_int(int(color_hex, 16))), ctypes.sizeof(ctypes.c_int))

# Change title bar color to dark purple
set_window_title_bar_color("#8f5beb")  # Use a hex color value without the '#'

# Run the application
root.mainloop()
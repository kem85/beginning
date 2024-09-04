import tkinter as tk
import ctypes
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.geometry("400x300")
root.title("Custom Title Bar Color")

# Function to apply the Windows accent color to the title bar
def apply_accent_color():
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    accent_color = 0x001D1D1D  # Dark gray as an example
    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 19, ctypes.byref(ctypes.c_int(accent_color)), ctypes.sizeof(ctypes.c_int))

apply_accent_color()

# Run the application
root.mainloop()
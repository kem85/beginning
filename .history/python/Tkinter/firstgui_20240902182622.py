import tkinter as tk
import ctypes

# Create the main application window
root = tk.Tk()
root.geometry("400x300")
root.title("Dark Mode Title Bar")

# Function to enable dark mode title bar (Windows 10+ only)
def apply_dark_mode_title_bar():
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(ctypes.c_int(1)), ctypes.sizeof(ctypes.c_int))

# Apply dark mode title bar
apply_dark_mode_title_bar()

# Run the application
root.mainloop()

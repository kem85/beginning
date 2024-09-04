import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *

root = tb.Window(themename="vapor")
root.title("Button Placement Example")
root.geometry('500x600')  # Set a fixed size to ensure visibility

# Function to add buttons
def add_buttons():
    for i in range(50):
        button = tb.Button(root, text=f'Pablo {i}', takefocus=False, width=15, style="PRIMARY")
        button.place(x=10, y=i * 30)  # Adjust `y` coordinate to place buttons vertically

# Call the function to add buttons
add_buttons()

root.mainloop()

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Create the main application window
root = ttk.Window(themename="darkly", title="Custom Title Bar")

# Create a frame to simulate the title bar
title_bar = ttk.Frame(root, bootstyle="dark", padding=5)
title_bar.pack(fill='x')

# Add a label to the simulated title bar
title_label = ttk.Label(title_bar, text="My Application", foreground="#FFD700", font=("Helvetica", 14))
title_label.pack(side='left', padx=10)

# Add a close button (you can also add minimize/maximize buttons)
close_button = ttk.Button(title_bar, text="X", command=root.destroy, bootstyle="danger")
close_button.pack(side='right')

# Create the main content area
content = ttk.Frame(root, padding=10)
content.pack(expand=True, fill='both')

# Run the application
root.mainloop()

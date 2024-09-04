import tkinter as tk
from tkinter import ttk

# Create the Tkinter window
root = tk.Tk()
root.title("Round Button Example")

# Create a Bootstrap-styled frame (optional)
frame = ttk.Frame(root, style="TFrame")
frame.pack(fill=tk.BOTH, expand=True)

# Define a custom style for the round button
style = ttk.Style()
style.theme_use("clam")  # Choose a theme (e.g., clam, default, alt)
style.configure("RoundButton.TButton", background="blue", foreground="white", padding=10, borderwidth=5, relief="flat")  # Adjust as needed

# Create the round button
button = ttk.Button(frame if frame else root, style="RoundButton.TButton", text="Click Me")
button.pack(pady=20)

# Run the application
root.mainloop()
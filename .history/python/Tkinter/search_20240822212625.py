import tkinter as tk

def on_mousewheel(event):
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def update_scrollregion():
    my_canvas.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

root = tk.Tk()
root.title("Simple Example")
root.iconbitmap('skills.ico')  # Optional, if you have an icon file
windowWidth = 400
windowHeight = 600
root.geometry(f'{windowWidth}x{windowHeight}')

# Main Frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

# Canvas
my_canvas = tk.Canvas(main_frame, bg="white")
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Scrollbar for the canvas
my_scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)

# Create a frame inside the canvas
second_frame = tk.Frame(my_canvas, bg="lightgrey")
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Add a few buttons to the frame
for i in range(50):
    button = tk.Button(second_frame, text=f'Button {i}', width=15)
    button.place(x=10, y=i * 30)

# Update scroll region to include all buttons
update_scrollregion()

# Bind mouse wheel scrolling
root.bind_all("<MouseWheel>", on_mousewheel)

root.mainloop()

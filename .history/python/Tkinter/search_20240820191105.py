import tkinter as tk

def on_text_change(*args):
    # Get the current text in the text box
    current_text = text_var.get()
    print("Text changed:", current_text)
    # Add your function logic here

root = tk.Tk()
root.title("Text Change Example")

# Create a StringVar to hold the text
text_var = tk.StringVar()

# Create a text box and associate it with the StringVar
text_box = tk.Entry(root, textvariable=text_var)
text_box.pack(padx=10, pady=10)

# Trace changes in the StringVar
text_var.trace_add("write", on_text_change)

root.mainloop()
import tkinter as tk

def on_text_change(*args):
    # Get the current text in the text box
    search_text = search_var.get().lower()
    
    # Clear the listbox
    listbox.delete(0, tk.END)
    
    # Search for matches and add to the listbox
    for item in items:
        if search_text in item.lower():
            listbox.insert(tk.END, item)

# Create the main window
root = tk.Tk()
root.title("Search Box Example")

# Predefined list of items to search from
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew"]

# Create a StringVar to hold the search text
search_var = tk.StringVar()

# Create a text box for the search input and associate it with the StringVar
search_box = tk.Entry(root, textvariable=search_var)
search_box.pack(padx=10, pady=10)

# Create a listbox to display the search results
listbox = tk.Listbox(root)
listbox.pack(padx=10, pady=10)

# Bind the StringVar to call on_text_change whenever the text changes
search_var.trace_add("write", on_text_change)

# Run the main event loop
root.mainloop()

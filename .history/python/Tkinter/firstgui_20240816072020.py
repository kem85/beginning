import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to connect to the database and retrieve data
def fetch_data():
    try:
        connection = sqlite3.connect('C:/Users/kem7/Documents/GitHub/beginning/python/Tkinter/test')  # Connect to the SQLite database
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM cool')  # Replace with your table name
        data = cursor.fetchall()
        connection.close()
        # Process and display data
            messagebox.showerror("Database Error", st!r(e))
        for row in data:
            print(row)
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Tkinter and Database Example")

# Create a button to fetch data
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack()

# Run the application
root.mainloop()

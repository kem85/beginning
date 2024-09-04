import tkinter as tk
from tkinter import messagebox
import sqlite3  # Use pymysql, psycopg2, etc., if connecting to other databases

def connect_to_db():
    try:
        # Connect to your database
        conn = sqlite3.connect('database.db')  # Replace with your database path for SQLite
        # For MySQL or PostgreSQL, you'd use pymysql.connect(...) or psycopg2.connect(...)
        
        messagebox.showinfo("Connection Status", "Connected to the database successfully!")
        return conn
    except Exception as e:
        messagebox.showerror("Connection Status", f"Failed to connect to the database: {e}")

def execute_query():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "SELECT * database"  # Replace with your actual query and table name
    cursor.execute(query)
    results = cursor.fetchall()
    
    result_text = "\n".join([str(row) for row in results])
    
    result_label.config(text=result_text)  # Display the results in the Tkinter window
    
    conn.close()

# Set up the Tkinter window
root = tk.Tk()
root.title("Database Connection Example")

# Add a button to connect to the database
connect_button = tk.Button(root, text="Connect to Database", command=execute_query)
connect_button.pack(pady=20)

# Add a label to display query results
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

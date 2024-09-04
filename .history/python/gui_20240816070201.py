import tkinter as tk
from tkinter import messagebox
import pymysql

def connect_to_db():
    try:
        # Replace these parameters with your actual database credentials
        connection = pymysql.connect(
            host="your_host",       # e.g., "localhost" or IP address
            user="your_user",       # e.g., "root"
            password="your_password", # your MySQL password
            database="your_database"  # the name of your database
        )
        messagebox.showinfo("Connection Status", "Connected to the database successfully!")
        return connection
    except Exception as e:
        messagebox.showerror("Connection Status", f"Failed to connect to the database: {e}")
        return None

def execute_query():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        
        # Replace with your actual SQL query
        query = "SELECT * FROM your_table_name"
        cursor.execute(query)
        results = cursor.fetchall()
        
        # Display the results in the Tkinter window
        result_text = "\n".join([str(row) for row in results])
        result_label.config(text=result_text)
        
        conn.close()

# Set up the Tkinter window
root = tk.Tk()
root.title("MySQL Database Connection")

# Add a button to connect to the database and run a query
connect_button = tk.Button(root, text="Connect to Database", command=execute_query)
connect_button.pack(pady=20)

# Add a label to display query results
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

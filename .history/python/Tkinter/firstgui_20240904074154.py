import tkinter as tk
from tkinter import messagebox, Toplevel, Frame, BOTH, LEFT, RIGHT, VERTICAL, Y
import ttkbootstrap as tb
from ttkbootstrap.constants import PRIMARY
import sqlite3

# Set up the database connection
conn = sqlite3.connect('accounts.db')
cun = conn.cursor()

# Initialize options list
options = []

# Update the options for the Combobox
def update_combobox():
    cun.execute('''SELECT name FROM database WHERE cata == 'false' ''')
    options.clear()
    for i in cun:
        options.append(i)

update_combobox()

# Initialize the main window
root = tb.Window(themename="vapor")

# Variable declarations
text_var = tk.StringVar()
name_var = tk.StringVar()
email_var = tk.StringVar()
color_var = tk.StringVar()
id_var = tk.StringVar()
poscat_var = tk.IntVar()
posbut_var = tk.IntVar()
password_var = tk.StringVar()
catagory_var = tk.IntVar()

buttons = tb.Style()
buttons.configure('Custom.TButton', font=('Helvetica', 12), foreground='#C0C0C0')

# Handle mouse wheel scrolling
def on_mousewheel(event):
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Update the scroll region
def update_scrollregion():
    my_canvas.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

# Function to add a new account
def ADD():
    # Your ADD functionality here
    pass

# Function to edit an account
def EDIT():
    # Your EDIT functionality here
    pass

# Database handling function
def database(name, email, password, color, catagory, id):
    cun.execute('''CREATE TABLE IF NOT EXISTS database (
    cata     TEXT,
    ID       TEXT,
    [order]  TEXT,
    name     TEXT,
    email    TEXT,
    password TEXT,
    color    TEXT DEFAULT ('6e40c0') 
);''')
    sql = ''' INSERT INTO database(name,email,password,color,cata,ID)
              VALUES(?,?,?,?,?,?) '''
    comm = [(name, email, password, color, catagory, id)]
    cun.executemany(sql, comm)
    conn.commit()

# Read data from the database
def readbase(indic):
    if indic == "countc":
        cun.execute('''
                    SELECT COUNT(cata) FROM database WHERE cata == 'false'
                    ''')
        return cun.fetchone()[0]
    elif indic == "countb":
        cun.execute('''
                    SELECT COUNT(cata) FROM database WHERE cata != 'false'
                    ''')
        return cun.fetchone()[0]

# Function to create buttons based on the database contents
def windowcreate(indic, update=False):
    global poscat_var, posbut_var
    if indic == 'catagory':
        if not update:
            for i in range(readbase('countc')):
                button = tb.Button(second_frame, text=f'Button {i}', takefocus=False, width=13, style='Custom.TButton')
                button.pack(pady=5, padx=10, anchor='w')
                poscat_var.set(i + 1)
        else:
            button = tb.Button(second_frame, text=f'Button {poscat_var.get()}', takefocus=False, width=13, style='Custom.TButton')
            button.pack(pady=5, padx=10, anchor='w')
            poscat_var.set(poscat_var.get() + 1)
        update_scrollregion()

addwindow = tk.BooleanVar()
editwindow = tk.BooleanVar()

# Set up the main window
root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 340
windowHeight = 450
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth / 2 - windowWidth / 2)
centerY = int(screenHeight / 2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(False, False)

# Create the main frame and canvas
main_frame = tb.Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = tb.Canvas(main_frame, width=100, height=405, bg='#110833')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scrollbar to the canvas
my_scrollbar = tb.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind_all("<MouseWheel>", on_mousewheel)

# Create a second frame inside the canvas
second_frame = Frame(my_canvas, width=340, bg='#110833')
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Add search, edit, and add buttons
search = tb.Entry(root, textvariable=text_var, width=30)
edit = tb.Button(root, text='Edit', takefocus=False, width=5, style=PRIMARY, command=lambda: EDIT())
edit.pack(side='right', anchor='e')
search.pack(side='right', anchor='w', expand=True, padx=15, pady=5)
add = tb.Button(root, text='Add', takefocus=False, width=5, style=PRIMARY, command=lambda: ADD())
add.pack(side='left', anchor='e')

# Initialize buttons and scroll region
windowcreate('catagory')
update_scrollregion()

# Start the main event loop
root.mainloop()

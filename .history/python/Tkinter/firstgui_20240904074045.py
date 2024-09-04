import tkinter as tk
from tkinter import messagebox
from tkinter import BooleanVar, Toplevel, Frame, BOTH, LEFT, RIGHT, VERTICAL, Y
import ttkbootstrap as tb
from ttkbootstrap.constants import PRIMARY
import sqlite3

conn = sqlite3.connect('accounts.db')
cun = conn.cursor()

options = []

def update_combobox():
    cun.execute('''SELECT name FROM database WHERE cata == 'false' ''')
    options.clear()
    for i in cun:
        options.append(i)

update_combobox()

root = tb.Window(themename="vapor")

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

def on_text_change(*args):  # search
    index = 0
    curt = text_var.get()
    nlst = [word[:-(len(word)-len(curt))] if len(word) > len(curt) else word for word in lst]  # lst is the names
    for i, cur in enumerate(nlst):
        if cur.lower() == curt.lower() and len(curt) != 0:
            pass

def on_mousewheel(event):  # scrolling
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def update_scrollregion():  # update 4 scrolling
    my_canvas.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

def ADD():
    # Your ADD functionality here
    pass

def EDIT():
    # Your EDIT functionality here
    pass

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

def windowcreate(indic, update=False):
    global poscat_var, posbut_var
    if indic == 'catagory':
        if not update:
            for i in range(readbase('countc')):
                button = tb.Button(second_frame, text=f'Button {i}', takefocus=False, width=13, style='Custom.TButton')
                if i % 2 == 0:
                    button.place(x=10, y=i*35)
                else:
                    button.place(x=180, y=(i-1)*35)
                if i == readbase('countc') - 1:
                    poscat_var.set(i + 2)
        else:
            button = tb.Button(second_frame, text=f'Button {poscat_var.get()}', takefocus=False, width=13, style='Custom.TButton')
            if poscat_var.get() % 2 == 0:
                button.place(x=10, y=poscat_var.get() * 35)
            else:
                button.place(x=180, y=(poscat_var.get() - 1) * 35)
        update_scrollregion()

addwindow = BooleanVar()
editwindow = BooleanVar()

#####################################################################
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
#####################################################################
main_frame = tb.Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = tb.Canvas(main_frame, width=100, height=405)
root.configure(bg='#110833')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = tb.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)

second_frame = Frame(my_canvas, width=340, height=readbase('countc')*35)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

#####################################################################
search = tb.Entry(root, textvariable=text_var, width=30)
edit = tb.Button(root, text='Edit', takefocus=False, width=5, style=PRIMARY, command=lambda: EDIT())
edit.pack(side='right', anchor='e')
search.pack(side='right', anchor='w', expand=True, padx=15, pady=5)
add = tb.Button(root, text='Add', takefocus=False, width=5, style=PRIMARY, command=lambda: ADD())
add.pack(side='left', anchor='e')

# Update scroll region to include all buttons
windowcreate('catagory')
update_scrollregion()

# Bind mouse wheel scrolling
my_canvas.bind_all("<MouseWheel>", on_mousewheel)

root.mainloop()

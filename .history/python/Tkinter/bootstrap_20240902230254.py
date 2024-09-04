import tkinter as tk
from tkinter import BooleanVar, Toplevel, Frame, BOTH, LEFT, RIGHT, VERTICAL, Y
import ttkbootstrap as tb
from ttkbootstrap.constants import PRIMARY
import sqlite3
conn = sqlite3.connect('accounts.db')
cun = conn.cursor()
root = tb.Window(themename="vapor")
text_var = tk.StringVar()
catagory = tk.IntVar()
style = tb.Style()
style.configure('Custom.TButton', font=('Helvetica', 18),foreground='#C0C0C0')
def on_text_change(*args): #search
    index = 0
    curt = text_var.get()
    nlst = [word[:-(len(word)-len(curt))] if len(word) > len(curt) else word for word in lst]
    for i,cur in enumerate(nlst):
        if cur.lower() == curt.lower() and len(curt)!=0:
            pass
def on_mousewheel(event): #scrolling
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
def update_scrollregion(): #update 4 scrolling
    my_canvas.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))
def ADD():
    global addwindow,editwindow
    if not addwindow.get() and not editwindow.get():
        addwindow.set(True)
        addacc = Toplevel(root)
        addacc.title("Add Account")
        deffont = ('Helvetica', 18)
        windowWidth = 450
        windowHeight = 300
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        centerX = int(screenWidth/2 - windowWidth / 2)
        centerY = int(screenHeight/2 - windowHeight / 2)
        addacc.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
        root.resizable(False, False)
        addacc.protocol("WM_DELETE_WINDOW", lambda: (addwindow.set(False) , addacc.destroy()))
        Name_Label = tb.Label(addacc, text='Name:',style=PRIMARY,font=deffont,foreground="#C0C0C0").grid(column=0,row=0)
        Password_Label = tb.Label(addacc, text='Password:',style=PRIMARY,font=deffont,foreground="#C0C0C0").grid(column=0,row=2)
        Color_Label = tb.Label(addacc, text='Color:',style=PRIMARY,font=deffont,foreground="#C0C0C0").grid(column=0,row=3)
        Name_Entry = tb.Entry(addacc,width=20,font=deffont).grid(column=1,row=0,pady=10,padx=10)
        Email_Label = tb.Label(addacc, text='Email:',style=PRIMARY,font=deffont,foreground="#C0C0C0").grid(column=0,row=1)
        Email_Entry = tb.Entry(addacc,width=20,font=deffont).grid(column=1,row=1,pady=10,padx=10)
        Password_Entry = tb.Entry(addacc,width=20,font=deffont).grid(column=1,row=2,pady=10,padx=10)
        Color_Entry = tb.Entry(addacc,width=20,font=deffont).grid(column=1,row=3,pady=10,padx=10)
        style = tb.Style()
        style.configure('Custom.TCheckbutton', font=('Helvetica', 18),foreground='#C0C0C0')
        Catagory = tb.Checkbutton(addacc,width=20,text="Catagory",onvalue=1,offvalue=0,style='Custom.TCheckbutton').grid(column=1,row=4,pady=10,padx=10)
        Submit = tb.Button(addacc,takefocus=False,width=15,style='Custom.TButton',text="Submit").grid(column=0,row=4,pady=10,padx=10)
def EDIT():
    global editwindow,addwindow
    if not editwindow.get() and not addwindow.get():
        editwindow.set(True)
        editacc = Toplevel(root)
        windowWidth = 450
        windowHeight = 300
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        centerX = int(screenWidth/2 - windowWidth / 2)
        centerY = int(screenHeight/2 - windowHeight / 2)
        editacc.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
        root.resizable(False, False)
        editacc.protocol("WM_DELETE_WINDOW", lambda: (editwindow.set(False) , editacc.destroy()))
def database():
    cun.execute('''CREATE TABLE IF NOT EXISTS database (
    cata     TEXT,
    ID       TEXT,
    [order]  TEXT,
    suborder TEXT,
    name     TEXT,
    email    TEXT,
    password TEXT,
    color    TEXT DEFAULT ('6e40c0') 
);''')
addwindow = BooleanVar()
editwindow = BooleanVar()
#####################################################################
root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 333
windowHeight = 450
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
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
second_frame = Frame(my_canvas, width=300, height=45*35) #50*45, 45 is y for each button and 50 is number of button
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
#####################################################################
for i in range(45):
    button = tb.Button(second_frame, text=f'Button {i}',takefocus=False,width=15,style=PRIMARY)
    if i % 2 == 0:
        button.place(x=15, y=i*35)
    else:
        button.place(x=190, y=(i-1)*35)


search = tb.Entry(root, textvariable=text_var,width=30)
edit = tb.Button(root, text='Edit',takefocus=False,width=5,style=PRIMARY,command=lambda:EDIT())
edit.pack(side='right', anchor='e')
search.pack(side='right', anchor='w',expand=True,padx=15,pady=5)
add = tb.Button(root, text='Add',takefocus=False,width=5,style=PRIMARY,command=lambda:ADD())
add.pack(side='left', anchor='e')
# Update scroll region to include all buttons
update_scrollregion()

# Bind mouse wheel scrolling
my_canvas.bind_all("<MouseWheel>", on_mousewheel)
text_var.trace_add("write", on_text_change)
root.mainloop()

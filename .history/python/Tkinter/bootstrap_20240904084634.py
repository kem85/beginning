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
posbut_var =tk.IntVar()
password_var = tk.StringVar()
catagory_var = tk.IntVar()
buttons= tb.Style()
buttonss = []
buttons.configure('Custom.TButton', font=('Helvetica', 12),foreground='#C0C0C0')
def on_text_change(*args): #search
    index = 0
    curt = text_var.get()
    nlst = [word[:-(len(word)-len(curt))] if len(word) > len(curt) else word for word in lst] #lst is the names
    for i,cur in enumerate(nlst):
        if cur.lower() == curt.lower() and len(curt)!=0:
            pass
def on_mousewheel(event): #scrolling
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
def update_scrollregion(): #update 4 scrolling
    min_height = 500  
    my_canvas.update_idletasks()
    bbox = my_canvas.bbox("all")
    my_canvas.configure(scrollregion=(bbox[0], bbox[1], bbox[2], max(bbox[3], min_height)))

def ADD():
    def clear(cond):
        if cond == 0:
            if ((len(color_var.get()) == 6) or color_var.get() == "") and name_var.get() != "" and ((email_var.get() != "" and password_var.get() !="" and Combo_Box.get() != "") or catagory_var.get()):
                messagebox.showinfo(title="Successful", message="Added account successfully")
                if readbase("countc") != 0 and catagory_var.get():
                    id_var.set(f"{readbase("countc")+1}")
                elif catagory_var.get():
                    id_var.set("1")
                else:
                    count = 1
                    cun.execute("SELECT ID FROM database WHERE name = ?", (Combo_Box.get(),))
                    ID = cun.fetchone()[0]
                    cun.execute("SELECT ID FROM database WHERE LENGTH(ID) >= 2")
                    for i in cun:
                        if i[0][0] == ID:
                            count += 1
                    id_var.set(f"{ID}/{count}")
                database(name_var.get(),email_var.get(),password_var.get(),color_var.get() or "6e40c0",Combo_Box.get() or "false",id_var.get())
                update_combobox()
                Combo_Box.configure(values=options)
                windowcreate('catagory',True)
            else:
                messagebox.showerror("Unsuccessful", "Invaild Format") 
            name_var.set("")
            color_var.set("")
            email_var.set("")
            password_var.set("")
        elif cond==1 and catagory_var.get() == 1:
            Combo_Box.set("")
            Email_Label.grid_remove()
            Email_Entry.grid_remove()
            Password_Label.grid_remove()
            Password_Entry.grid_remove()
            Combo_Box.place_forget()
        elif cond == 1 and catagory_var.get() == 0:
            Email_Label.grid()
            Email_Entry.grid()
            Password_Label.grid()
            Password_Entry.grid()
            Combo_Box.place(x=269,y=260)
    global addwindow,editwindow
    if not addwindow.get() and not editwindow.get():
        addwindow.set(True)
        addacc = Toplevel(root)
        addacc.title("Add Account")
        deffont = ('Helvetica', 18)
        windowWidth = 425
        windowHeight = 300
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        centerX = int(screenWidth/2 - windowWidth / 2)
        centerY = int(screenHeight/2 - windowHeight / 2)
        addacc.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
        root.resizable(False, False)
        addacc.protocol("WM_DELETE_WINDOW", lambda: (addwindow.set(False) , addacc.destroy()))
        Name_Label = tb.Label(addacc, text='Name:',style=PRIMARY,font=deffont,foreground="#C0C0C0")
        Name_Label.grid(column=0,row=0)
        Email_Label = tb.Label(addacc, text='Email:',style=PRIMARY,font=deffont,foreground="#C0C0C0")
        Email_Label.grid(column=0,row=1)
        Password_Label = tb.Label(addacc, text='Password:',style=PRIMARY,font=deffont,foreground="#C0C0C0")
        Password_Label.grid(column=0,row=2)
        Color_Label = tb.Label(addacc, text='Color:',style=PRIMARY,font=deffont,foreground="#C0C0C0")
        Color_Label.grid(column=0,row=3)
        Name_Entry = tb.Entry(addacc,width=15,textvariable=name_var,font=deffont)
        Email_Entry = tb.Entry(addacc,width=15,font=deffont,textvariable=email_var)
        Password_Entry = tb.Entry(addacc,width=15,font=deffont,textvariable=password_var)
        Color_Entry = tb.Entry(addacc,width=15,font=deffont,textvariable=color_var)
        Name_Entry.grid(column=1,row=0,pady=10,padx=5)
        Email_Entry.grid(column=1,row=1,pady=10,padx=5)
        Password_Entry.grid(column=1,row=2,pady=10,padx=5)
        Color_Entry.grid(column=1,row=3,pady=10,padx=5)
        addacc.option_add('*TCombobox*Listbox.font', ('Helvetica', 14))
        Combo_Box = tb.Combobox(addacc,values=options,font=('Helvetica', 14),width=10)
        style = tb.Style()
        style.configure('Custom.TCheckbutton', font=('Helvetica', 18),foreground='#C0C0C0')
        Catagory = tb.Checkbutton(addacc,width=10,text="Catagory",onvalue=1,offvalue=0,style='Custom.TCheckbutton',variable=catagory_var,command=lambda:clear(1))
        Submit = tb.Button(addacc,takefocus=False,width=10,style='Custom.TButton',text="Submit",command=lambda:(clear(0)))
        Catagory.place(x=10,y=260)
        Combo_Box.place(x=269,y=260)
        Submit.place(x=135,y=260)
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
def database(name,email,password,color, catagory,id):
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
    comm = [(name, email, password,color,catagory,id),]
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
def windowcreate(indic,update = False):
    global poscat_var,posbut_var,buttonss
    if indic == 'catagory':
            greg = False
            if update:
                for button in buttonss:
                 button.place_forget()
                greg = True
            buttonss.clear()
            for i in range(readbase('countc')): #45 buttons
                button = tb.Button(second_frame, text=f'Button {i}',takefocus=False,width=13,style='Custom.TButton')
                button.place(x=180, y=(i-1)*35)
                buttonss.append(button)
            update_scrollregion()
            second_frame.update_idletasks()
            if greg:
                asd = tb.Combobox(second_frame,text="GERRR",width=15).pack
    else:
        pass
addwindow = BooleanVar()
editwindow = BooleanVar()
#####################################################################
root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 340
windowHeight = 450
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
# root.resizable(False, False)
#####################################################################
main_frame = tb.Frame(root)
main_frame.pack(fill=BOTH, expand=1)
my_canvas = tb.Canvas(main_frame, width=100, height=405)
root.configure(bg='#110833')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_scrollbar = tb.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
second_frame = Frame(my_canvas, width=340, height=readbase('countc')*35) #50*45, 45 is y for each button and 50 is number of button
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
#####################################################################


search = tb.Entry(root, textvariable=text_var,width=30)
edit = tb.Button(root, text='Edit',takefocus=False,width=5,style=PRIMARY,command=lambda:EDIT())
edit.pack(side='right', anchor='e')
search.pack(side='right', anchor='w',expand=True,padx=15,pady=5)
add = tb.Button(root, text='Add',takefocus=False,width=5,style=PRIMARY,command=lambda:ADD())
add.pack(side='left', anchor='e')
# Update scroll region to include all buttons
windowcreate('catagory')
update_scrollregion()
# Bind mouse wheel scrolling
my_canvas.bind_all("<MouseWheel>", on_mousewheel)
text_var.trace_add("write", on_text_change)
root.mainloop()

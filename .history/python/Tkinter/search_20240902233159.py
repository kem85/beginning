from tkinter import messagebox, ttk
import tkinter as tk
from tkinter import *
root = Tk()
root.resizable(0, 0)
root.eval('tk::PlaceWindow . center')
name_var=StringVar()
passw_var=StringVar()
name_var1=StringVar()
passw_var1=StringVar()
num1=StringVar()
lst = []
def convert(first,second, windows10=None):
    labol1 = Label(windows10,text = "Result: ",width=5,height =5,font = ('calibre',10,'normal'))
    result = Listbox(windows10,height=2,font = ('calibre',15,'normal'))
    g = int(num1.get())
    n = 4
    binary11 = format(n, 'b')
    if first == "Decimal" and second == "Binary":
        binary = bin(g)
        labol1.grid(row = 2,column=0)
        result.grid(row = 2,column=1)
        result.insert(END,f"{binary}"[2:])
    elif first == "Binary" and second == "Decimal":
        binary11 = num1.get()
        decimal = int(binary11, 2)
        labol1.grid(row = 2,column=0)
        result.grid(row = 2,column=1)
        result.insert(END,f"{decimal}")
    elif first == "Octal" and second == "Decimal":
         decimal = int(str(num1.get()), 8); 
         labol1.grid(row = 2,column=0)
         result.grid(row = 2,column=1)
         result.insert(END,f"{decimal}")
    elif first == "Decimal" and second == "Octal":
        octal = oct(g)
        labol1.grid(row = 2,column=0)
        result.grid(row = 2,column=1)
        result.insert(END,f"{octal}"[2:])
    elif first == "Octal" and second == "Binary":
        decimal = int(str(num1.get()), 8);
        binary = bin(decimal)
        labol1.grid(row = 2,column=0)
        result.grid(row = 2,column=1)
        result.insert(END,f"{binary}"[2:])
    elif first == "Binary" and second == "Octal":
        binary11 = num1.get()
        octal = oct(binary11)
        labol1.grid(row = 2,column=0)
        result.grid(row = 2,column=1)
        result.insert(END,f"{octal}"[2:])
    else:
        messagebox.showerror("Error","Cant select Both the same")
def form():
    newWindow1 = Toplevel(root)
    root.withdraw()
    newWindow1.resizable(0, 0)
    newWindow1.title("App")
    combo = ttk.Combobox(
    newWindow1,
    state="readonly",
    values=["Binary", "Decimal", "Octal"],
    width = 15,
    height = 5)
    combo1 = ttk.Combobox(
    newWindow1,
    state="readonly",
    values=["Binary", "Decimal", "Octal"],
    width = 15,
    height = 5)
    labol = Label(newWindow1,text = " To ",width=5,height =5,font = ('calibre',15,'normal'))
    submot = Button(newWindow1, text="Convert", width=10,height=2,font = ('calibre',15,'normal'),command = lambda:convert(combo.get(),combo1.get(),newWindow1))
    num = Entry(newWindow1,textvariable = num1, font=('calibre',15,'normal'))
    num.grid(row=1,column=1)
    combo.grid(row = 0, column=0,sticky=W,pady=3)
    labol.grid(row = 0,column=1)
    combo1.grid(row = 0, column=2,sticky=W,pady=3)
    submot.grid(row = 3, column=1)
def submit(num, window = None):
    if num == "login":
        file1 = open("data.txt", "r+")
        name=name_var.get() or " "
        password=passw_var.get() or " " 
        lst = file1.readlines(0)
        for i in range(len(lst)):
            lst[i] = lst[i].strip("\n")
        count = 0
        g = True
        try:
           for i in range(len(lst)):
               if name == lst[i] and password ==lst[i+1] and count <=2:
                   messagebox.showinfo(title="successful", message="logged in successfully")
                   form()
                   lst.append("true")
                   break
               else:
                   if g:
                     count = 3
                     g = False
                   else:
                       g = True
                       count = 1
        except IndexError:
            messagebox.showerror("unsuccessful", "Wrong Username or Password")
            lst.append("true")
        if lst[len(lst)-1] != "true":
            messagebox.showerror("unsuccessful", "Wrong Username or Password") 

        file1.close()
        name_var.set("")
        passw_var.set("")
    if num == "register":
        file1 = open("data.txt", "a")
        name1=name_var1.get()
        password1=passw_var1.get()
        if name1 and password1 != "":
            if len(password1) >= 8:
                root.deiconify()
                file1.write(f"{name1}\n")
                file1.writelines(f"{password1}\n")
                file1.close() 
                name_var1.set("")
                passw_var1.set("")
                if window:
                    window.destroy()
            else:
                messagebox.showerror("unsuccessful", "Password must be higher than 8")
        else:
            messagebox.showerror("unsuccessful", "Invaild Format")

def regstr():
    newWindow = Toplevel(root)
    newWindow.resizable(0, 0)
    newWindow.title("Register")
    username = Label(newWindow,text="Username: ")
    name_entry = Entry(newWindow,textvariable = name_var1, font=('calibre',15,'normal'))
    password = Label(newWindow,text="Password: ")
    passw_entry=Entry(newWindow, textvariable = passw_var1, font = ('calibre',15,'normal'), show = '*')
    sub_btn=Button(newWindow,text = 'Signup', command = lambda: submit("register", newWindow))
    username.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    password.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)
root.title("Login")
username = Label(root,text="Username: ")
name_entry = Entry(root,textvariable = name_var, font=('calibre',15,'normal'))
password = Label(root,text="Password: ")
passw_entry=Entry(root, textvariable = passw_var, font = ('calibre',15,'normal'), show = '*')
sub_btn=Button(root,text = 'Login', command = lambda: submit("login"))
register=Button(root,text = 'Register', command = lambda: [regstr(), root.withdraw()])
username.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
password.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
register.grid(row=2,column=0)
mainloop()
from tkinter import *
import sqlite3

root = Tk()
root.wm_attributes('-fullscreen','true')
root.title("My Test GUI")


Fullname=StringVar()

conn = sqlite3.connect('gaga.db')
cursor=conn.cursor()

def database():

   name1=Fullname.get()

   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT)')
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT)')

   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT)')

   cursor.execute('INSERT INTO Student (FullName) VALUES(?)',(name1,))

   conn.commit()

def error():

    root1 = Toplevel(root)
    root1.geometry("150x90")
    root1.title("Warning")
    Label(root1, text = "All fields required", fg = "red").pack()

def read_from_db():
    cursor.execute('SELECT * FROM Student')
    data = cursor.fetchall()
    print(data)

label_0 = Label(root, text="My Test GUI",width=20,font=("bold", 20))
label_0.place(x=650,y=53)


label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=550,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=700,y=130)

Button(root, text='Submit',width=20,bg='brown',fg='white', command=database).place(x=650,y=380)

root.mainloop()
read_from_db()
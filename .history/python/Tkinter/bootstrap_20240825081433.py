import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
from tkinter import *
root = tb.Window(themename="vapor")
text_var = tk.StringVar()
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
    global windowIsOpen
    if not windowIsOpen.get():
        windowIsOpen.set(True)
        addacc = Toplevel(root)
        windowWidth = 450
        windowHeight = 300
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        centerX = int(screenWidth/2 - windowWidth / 2)
        centerY = int(screenHeight/2 - windowHeight / 2)
        addacc.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
        addacc.protocol("WM_DELETE_WINDOW", lambda: (windowIsOpen.set(False) , addacc.destroy()))

def EDIT():
     pass 
# Initialize the BooleanVar
windowIsOpen = BooleanVar()
#####################################################################
root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 300
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
second_frame = Frame(my_canvas, width=300, height=50*45) #50*45, 45 is y for each button and 50 is number of button
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
#####################################################################
# Add some buttons to the frame
for i in range(50):
    button = tb.Button(second_frame, text=f'Button {i}',takefocus=False,width=15,style=PRIMARY)
    button.place(x=100, y=i*45)

search = tb.Entry(root, textvariable=text_var,width=30)
edit = tb.Button(root, text='Add',takefocus=False,width=10,style=PRIMARY,command=lambda:ADD())
edit.pack(side='right', anchor='e')
search.pack(side='right', anchor='w',expand=True,padx=15,pady=5)
add = tb.Button(root, text='Add',takefocus=False,width=10,style=PRIMARY,command=lambda:ADD())
add.pack(side='left', anchor='e')
# Update scroll region to include all buttons
update_scrollregion()

# Bind mouse wheel scrolling
my_canvas.bind_all("<MouseWheel>", on_mousewheel)
text_var.trace_add("write", on_text_change)
root.mainloop()

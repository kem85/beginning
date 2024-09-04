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
def openNewWindow(dooler):
    global windowIsOpen

    if not windowIsOpen:
        windowIsOpen = True
        newWindow = Toplevel(root)
        newWindow.title("New Window")
        newWindow.geometry("200x200")
        Label(newWindow, 
               text="This is a new window").pack()


        # Check if the new window is open
        if newWindow.winfo_exists():
            print("New window is open")
        else:
            print("New window is closed or destroyed")

        # Reset the flag when the window is closed
        newWindow.protocol("WM_DELETE_WINDOW", command = lambda:open)
    else:
        print("New window is already open")

# Initialize the flag
windowIsOpen = False
#####################################################################
root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 400
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
second_frame = Frame(my_canvas, width=300, height=50*45)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
#####################################################################
# Add some buttons to the frame
for i in range(50):
    button = tb.Button(second_frame, text=f'Button {i}',takefocus=False,width=15,style=PRIMARY)
    button.place(x=100, y=i*45)

search = tb.Entry(root, textvariable=text_var,width=30)
search.pack(side='right', anchor='w',expand=True, padx=20,pady=5)
add = tb.Button(root, text='Add',takefocus=False,width=10,style=PRIMARY,command=lambda:openNewWindow())
add.pack(side='left', anchor='e')
# Update scroll region to include all buttons
update_scrollregion()

# Bind mouse wheel scrolling
my_canvas.bind_all("<MouseWheel>", on_mousewheel)
text_var.trace_add("write", on_text_change)
root.mainloop()

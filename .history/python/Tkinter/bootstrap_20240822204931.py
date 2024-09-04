import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *

root = tb.Window(themename="vapor")
rely = 1
text_var = tk.StringVar()
lst = ["gorilla","moshella","mushella","mosheila","garilla","boot","broooot","league","of","grame","abooo","league"]
def on_text_change(*args):
    index = 0
    curt = text_var.get()
    nlst = [word[:-(len(word)-len(curt))] if len(word) > len(curt) else word for word in lst]
    for i,cur in enumerate(nlst):
        if cur.lower() == curt.lower() and len(curt)!=0:
            print(lst[i])
def on_mousewheel(event):
   my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 400
windowHeight = 400
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
# root.resizable(False, False)
#Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=1)
#Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
#scrollbar 2 canvas
my_scrollbar = tb.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
#configure canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
root.bind_all("<MouseWheel>", on_mousewheel)
#create 2nd frame in canvas
second_frame = Frame(my_canvas)
my_canvas.create_window((0,0),window=second_frame,anchor="nw")
for i in range(50):
    button = tb.Button(second_frame,text=f'Pablo {i}').grid(column=2,row=i)
search = tb.Entry(root, textvariable=text_var,width="30")
search.pack(padx=10, pady=10)
text_var.trace_add("write", on_text_change)
root.mainloop()

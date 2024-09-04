import tkinter as tk
 
class MyCanvas(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
 
        self.container = tk.Frame(parent)
        self.container.grid(column=0, row=0, sticky='news')
        self.container.grid_columnconfigure(0, weight=3)
 
        self.canvas = tk.Canvas(self.container, bg='ivory')
        self.scrollbar = tk.Scrollbar(self.container, orient='vertical')
 
        self.canvas['yscrollcommand'] = self.scrollbar.set
        self.canvas['scrollregion'] = self.canvas.bbox('all')
        self.scrollbar['command'] = self.canvas.yview
 
        self.scrollbar.grid(column=1, row=0, sticky='ns')
        self.canvas.grid(column=0, row=0, sticky='news')
 
        self.frame = tk.Frame(self.canvas, bg='ivory')
        self.frame.grid(column=0, row=0, sticky='news')
 
        self.canvas.create_window(50, 10, window=self.frame, anchor='n')
 
 
 
class MyButton(tk.Button):
    def __init__(self, parent, text, col, row, command=None, *args, **kwargs):
        self.parent = parent
        super().__init__(*args, **kwargs)
        self.button = tk.Button(parent)
        self.button['text'] = text
        self.button['command'] = command
        self.button.grid(column=col, row=row, sticky='new', pady=4, padx=2)
 
 
root = tk.Tk()
root.geometry('+250+250')
canvas = MyCanvas(root)
col = 0
row = 0
for i in range(100):
    MyButton(canvas.frame, f'Button {i}', col, row)
    if col >= 4:
        row += 1
        col = 0
    else:
        col += 1
root.mainloop()
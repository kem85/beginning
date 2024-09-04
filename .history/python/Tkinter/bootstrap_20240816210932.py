import ttkbootstrap as tk
from ttkbootstrap.constants import *
root = tk.window()
text = tk.Text(root)
text.pack(side="left")
sb = tk.Scrollbar(root, command=text.yview)
sb.pack(side="right")
text.configure(yscrollcommand=sb.set)
...
for i in range(10):
    button = tk.Button(text, ...)
    text.window_create("end", window=button)
    text.insert("end", "\n")
text.configure(state="disabled")
root.mainloop()
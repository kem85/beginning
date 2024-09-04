import tkinter as tk

#Window
root = tk.Tk()
root.geometry("800x700")
root.title("Account Overview")

#Title_Frame
title_frame = tk.Frame(root, width=800, height=100, bg='#b1b7ba')
title_frame.pack(side='top')
title_label = tk.Label(title_frame, text="Account Overview", font='Courier 35 underline')
title_label.place(relx=0.2, rely=0.2)

#Account_Frame
account_frame = tk.Frame(root, width=300, height=700, bg='#9dd7f5')
account_frame.pack(side='right')
add_account_button = tk.Button(account_frame, text="Add Account", font='Courier 15')
add_account_button.place(relx=0.26, rely=0.03)
account = tk.Label(account_frame, text="Account Nr1", font='Helvetica 40')
account.place(relx=0.01, rely=0.125)

root.mainloop()
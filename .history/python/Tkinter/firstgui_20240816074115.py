import tkinter as tk
lbllst = []
def addlabel():
    account = tk.Label(account_frame, text="Account Nr"+str(len(lbllst)+1), font='Helvetica 40')
    account.place(relx=0.01, rely=0.125*(len(lbllst)+1))
    lbllst.append(account)
   
#Account_Frame
account_frame = tk.Frame(root, width=300, height=700, bg='#9dd7f5')
account_frame.pack(side='right')
add_account_button = tk.Button(account_frame, text="Add Account", font='Courier 15', command=addlabel)
add_account_button.place(relx=0.26, rely=0.03)

root.mainloop()
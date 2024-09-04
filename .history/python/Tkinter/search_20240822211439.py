for i in range(50):
    button = tb.Button(main_frame,text=f'Pablo {i}',takefocus=False,width=15,style=PRIMARY)
    button.place(rely=i,relx=5)
import customtkinter

from logic import *

# app instance
app = customtkinter.CTk()

# system screen size
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
custom_size = str(width) + 'x' + str(height)

# frame title
app.geometry(custom_size)
app.title('Lip Sync')

# first frame for title
title_frame = customtkinter.CTkFrame(master=app, width=width, bg_color='#880808', fg_color='#880808')
title_frame.pack(side='top', fill='x', expand=False, pady=0, padx=0)

title_text = customtkinter.CTkLabel(master=title_frame, text='LIP-SYNC', width=10, height=10, font=('Open Sans', 18, 'bold'))
title_text.pack(side='left', padx=20, ipadx=5, pady=20, ipady=10)

button = customtkinter.CTkButton(master=title_frame, text='Generate Sync Video', fg_color='#CC5500', hover_color='#CC5500', font=('Open Sans', 14), command=generate)
button.pack(side='right', padx=20, ipadx=5, pady=20, ipady=5)

# second frame
list_frame = customtkinter.CTkFrame(master=app, width=width, height=height, bg_color='#B9B2B2', fg_color='#B9B2B2')
list_frame.pack()


app.mainloop()
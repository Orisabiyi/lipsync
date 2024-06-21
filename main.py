import customtkinter

from logic import *

# app instance
app = customtkinter.CTk()

# system screen size
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
custom_size = str(width) + 'x' + str(height)

app.geometry(custom_size)
app.title('Lip Sync')

screen_center_horizontal = width / 2.2
screen_bottom_place = height - 200

button = customtkinter.CTkButton(master=app, text='Generate Sync Video', command=generate)
button.place(x=screen_center_horizontal, y=screen_bottom_place)


app.mainloop()
import customtkinter
from logic import *
from color import *

class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()

    # generating size based on user screen
    width = self.winfo_screenwidth()
    height = self.winfo_screenheight()
    custom_size = str(width) + 'x' + str(height)
    
    self.title('Lip Sync')
    self.geometry(custom_size)

    # header frame
    self.header_frame = customtkinter.CTkFrame(self, width=width, bg_color=PRIMARY_COLOR, fg_color=PRIMARY_COLOR)
    self.header_frame.pack(side='top', fill='x', expand=False, pady=0, padx=0)

    self.header_text_logo = customtkinter.CTkLabel(master=self.header_frame, text='LIP-SYNC', width=10, height=10, font=('Open Sans', 18, 'bold'))
    self.header_text_logo.pack(side='left', padx=20, ipadx=5, pady=20, ipady=10)

    self.header_btn = customtkinter.CTkButton(master=self.header_frame, text='Generate Sync Video', fg_color=PRIMARY_COLOR_2, hover_color=PRIMARY_COLOR_2, font=('Open Sans', 14), command=generate)
    self.header_btn.pack(side='right', padx=20, ipadx=5, pady=20, ipady=5)

    # content frame
    self.content_frame = customtkinter.CTkFrame(self, width=width, height=height, bg_color=SECONDARY_COLOR, fg_color=SECONDARY_COLOR)
    self.content_frame.pack()


app = App()
app.mainloop()

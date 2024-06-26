from tkinter import Scrollbar, VERTICAL
import customtkinter
from logic import *
from color import *


class App(customtkinter.CTk):

  def slider_value(self, value):
         self.label.configure(text=f"Value: {value}")

  def __init__(self):
    super().__init__()

    # generating size based on user screen
    self.width = self.winfo_screenwidth()
    self.height = self.winfo_screenheight()
    self.custom_size = str(self.width) + 'x' + str(self.height)

    # fonts
    self.font_14 = ('Open Sans', 14, 'bold')
    self.font_18 = ('Open Sans', 18, 'bold')
    
    self.title('Lip Sync')
    self.geometry(self.custom_size)

    def edit():
      self.history_parent_frame.pack_forget()


    # parent default frame
    self.history_parent_frame = customtkinter.CTkFrame(self, width=self.width, height=self.height)
    self.history_parent_frame.pack(side='top', fill='both', expand=True)
    # header frame
    self.header_frame = customtkinter.CTkFrame(self.history_parent_frame, width=self.width, bg_color=PRIMARY_COLOR, fg_color=PRIMARY_COLOR)
    self.header_frame.pack(side='top', fill='x', expand=False, pady=0, padx=0)

    self.header_text_logo = customtkinter.CTkLabel(self.header_frame, text='LIP-SYNC', width=10, height=10, font=self.font_18)
    self.header_text_logo.pack(side='left', padx=20, ipadx=5, pady=20, ipady=10)

    self.header_btn = customtkinter.CTkButton(self.header_frame, text='Generate Video', fg_color=PRIMARY_COLOR_3, hover_color=PRIMARY_COLOR_2, text_color=NEUTRAL_COLOR_1, font=self.font_14, corner_radius=20, command=edit)
    self.header_btn.pack(side='right', padx=20, pady=20, ipadx=5, ipady=5)

    # content frame
    self.content_frame = customtkinter.CTkScrollableFrame(self.history_parent_frame, width=self.width, height=self.height, bg_color=SECONDARY_COLOR, fg_color=SECONDARY_COLOR)
    self.content_frame.pack(side='bottom')

    # Now, you can add your content to self.scrollable_frame instead of self.content_frame
    self.welcome__label = customtkinter.CTkLabel(self.content_frame, text='Welcome to Lip Sync, Click the generate video button to sync a video to audio.', text_color=NEUTRAL_COLOR, font=self.font_14)
    self.welcome__label.pack(padx=10, pady=20)
    

# if __name__ == "__main__":
app = App()
app.mainloop()

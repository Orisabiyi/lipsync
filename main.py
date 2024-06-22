from tkinter import Scrollbar, VERTICAL
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

    self.header_text_logo = customtkinter.CTkLabel(self.header_frame, text='LIP-SYNC', width=10, height=10, font=('Open Sans', 18, 'bold'))
    self.header_text_logo.pack(side='left', padx=20, ipadx=5, pady=20, ipady=10)

    self.header_btn = customtkinter.CTkButton(self.header_frame, text='Generate Sync Video', fg_color=PRIMARY_COLOR_2, hover_color=PRIMARY_COLOR_3, text_color='#fff', font=('Open Sans', 15, 'bold'), corner_radius=20, command=generate)
    self.header_btn.pack(side='right', padx=20, ipadx=10, pady=20, ipady=10)

    # content frame
    self.canvas = customtkinter.CTkCanvas(self)
    self.canvas.pack(side='left', fill='both', expand=True)

    self.scrollbar = Scrollbar(self, orient=VERTICAL)
    # self.scrollbar.pack(side='right', fill='y')

    self.canvas.configure(background=SECONDARY_COLOR, yscrollcommand=self.scrollbar.set)
    self.scrollbar.config(command=self.canvas.yview)

    self.content_frame = customtkinter.CTkFrame(self.canvas, width=width, height=height, bg_color=SECONDARY_COLOR, fg_color=SECONDARY_COLOR)

    self.canvas_frame = self.canvas.create_window((0,0), window=self.content_frame, anchor='nw')

    # dynamic scroll region and canvas width configuration
    def configure_scroll_region(event):
      self.canvas.configure(scrollregion=self.canvas.bbox('all'))
      # Check if scrollbar should be visible
      if self.canvas.bbox('all')[3] > self.canvas.winfo_height():
          self.scrollbar.pack(side='right', fill='y')
      else:
          self.scrollbar.pack_forget()

    def configure_canvas_width(event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)

    self.content_frame.bind('<Configure>', configure_scroll_region)
    self.canvas.bind('<Configure>', configure_canvas_width)

    # Now, you can add your content to self.scrollable_frame instead of self.content_frame
    self.content_no_label = customtkinter.CTkLabel(self.content_frame, text='NO HISTORY YET, CLICK THE GENERATE BUTTON TO GENERATE A VIDEO', text_color='#000', font=('Open Sans', 16, 'bold'))
    self.content_no_label.pack(padx=10, pady=20)
    


app = App()
app.mainloop()

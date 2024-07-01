import customtkinter
from PIL import Image, ImageTk
import cv2

from color import *
from edit import edit


class App(customtkinter.CTk):
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

    # parent default frame
    self.history_parent_frame = customtkinter.CTkFrame(self, width=self.width, height=self.height)
    self.history_parent_frame.pack(side='top', fill='both', expand=True)

    # header frame
    self.header_frame = customtkinter.CTkFrame(self.history_parent_frame, width=self.width, bg_color=PRIMARY_COLOR, fg_color=PRIMARY_COLOR)
    self.header_frame.pack(side='top', fill='x', expand=False, pady=0, padx=0)

    self.header_text_logo = customtkinter.CTkLabel(self.header_frame, text='LIP-SYNC', width=10, height=10, font=self.font_18)
    self.header_text_logo.pack(side='left', padx=20, ipadx=5, pady=20, ipady=10)

    self.header_btn = customtkinter.CTkButton(self.header_frame, text='Generate Video', fg_color=PRIMARY_COLOR_3, hover_color=PRIMARY_COLOR_2, text_color=NEUTRAL_COLOR_1, font=self.font_14, corner_radius=20, command=lambda: edit(self))
    self.header_btn.pack(side='right', padx=20, pady=20, ipadx=5, ipady=5)

    # content frame
    self.content_frame = customtkinter.CTkScrollableFrame(self.history_parent_frame, width=self.width, height=self.height, bg_color=SECONDARY_COLOR, fg_color=SECONDARY_COLOR)
    self.content_frame.pack(side='bottom')

    # Now, you can add your content to self.scrollable_frame instead of self.content_frame
    self.welcome__label = customtkinter.CTkLabel(self.content_frame, text='Welcome to Lip Sync, Click the generate video button to sync a video to audio.', text_color=NEUTRAL_COLOR, font=self.font_14)
    self.welcome__label.pack(padx=10, pady=20)
      

  def open_video_image_dialog(self):
      file_types = (
          ("Image files", "*.jpg *.jpeg *.png"),
          ("Video files", "*.mp4 *.avi"),
      )

      file_obj = customtkinter.filedialog.askopenfile(title='Select files', filetypes=file_types)
      file_path = file_obj.name

      if file_obj:
        self.file_name_label.configure(text=f"Selected: {file_path}")
        self.display_preview(file_path)
      else:
          self.file_name_label.configure(text="No file selected")
          self.display_preview('')


  def open_audio_dialog(self):
      file_types = (
          ("Audio files", "*.mp3 *.wav *.aac"),
      )

      file_obj = customtkinter.filedialog.askopenfile(title='Select files', filetypes=file_types)

      if file_obj:
        self.file_audio_label.configure(text=f"Selected: {file_obj.name}")
      else:
          self.file_audio_label.configure(text="No file selected")


  def display_preview(self, file_path):
    if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):    
        img = Image.open(file_path)
        img.thumbnail((1000, 200))  # Resize for preview
        img_preview = ImageTk.PhotoImage(img)

        # Display image preview
        self.preview_label.configure(image=img_preview, text='')
        self.preview_label.image = img_preview  # Keep a reference
    elif file_path.lower().endswith(('.mp4', '.avi')):
        # Display video preview (first frame)
        cap = cv2.VideoCapture(file_path)
        ret, frame = cap.read()
        if ret:
            self.preview_label.configure(text="")
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img.thumbnail((1000, 200), Image.ANTIALIAS)  # Resize for preview
            img_preview = ImageTk.PhotoImage(img)
            self.preview_label.configure(image=img_preview, text='')
            self.preview_label.image = img_preview  # Keep a reference
        cap.release()

  def invoke(self):
      pass


# if __name__ == "__main__":
app = App()
app.mainloop()
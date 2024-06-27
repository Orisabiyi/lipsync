from tkinter import Scrollbar, VERTICAL
import customtkinter

from PIL import Image, ImageTk
import cv2
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

    # parent default frame
    self.history_parent_frame = customtkinter.CTkFrame(self, width=self.width, height=self.height)
    self.history_parent_frame.pack(side='top', fill='both', expand=True)
    # header frame
    self.header_frame = customtkinter.CTkFrame(self.history_parent_frame, width=self.width, bg_color=PRIMARY_COLOR, fg_color=PRIMARY_COLOR)
    self.header_frame.pack(side='top', fill='x', expand=False, pady=0, padx=0)

    self.header_text_logo = customtkinter.CTkLabel(self.header_frame, text='LIP-SYNC', width=10, height=10, font=self.font_18)
    self.header_text_logo.pack(side='left', padx=20, ipadx=5, pady=20, ipady=10)

    self.header_btn = customtkinter.CTkButton(self.header_frame, text='Generate Video', fg_color=PRIMARY_COLOR_3, hover_color=PRIMARY_COLOR_2, text_color=NEUTRAL_COLOR_1, font=self.font_14, corner_radius=20, command=self.edit)
    self.header_btn.pack(side='right', padx=20, pady=20, ipadx=5, ipady=5)

    # content frame
    self.content_frame = customtkinter.CTkScrollableFrame(self.history_parent_frame, width=self.width, height=self.height, bg_color=SECONDARY_COLOR, fg_color=SECONDARY_COLOR)
    self.content_frame.pack(side='bottom')

    # Now, you can add your content to self.scrollable_frame instead of self.content_frame
    self.welcome__label = customtkinter.CTkLabel(self.content_frame, text='Welcome to Lip Sync, Click the generate video button to sync a video to audio.', text_color=NEUTRAL_COLOR, font=self.font_14)
    self.welcome__label.pack(padx=10, pady=20)

  def edit(self):
      self.history_parent_frame.pack_forget()

      self.setting = customtkinter.CTkFrame(self, width=self.width / 2, height=self.height, fg_color=SECONDARY_COLOR)
      self.setting.pack(side='left', fill='both', expand=True)

      # model frame
      self.model_frame = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.model_frame.pack(side='top', pady=(20, 0), padx=20)
      self.model_frame.pack_propagate(flag=False)

      self.model_text = customtkinter.CTkLabel(self.model_frame, text='Select Model')
      self.model_text.pack(anchor='w', padx=(20, 0))

      self.model_select = customtkinter.CTkComboBox(self.model_frame, values=['wav2lip', 'wav2lip-gan'])
      self.model_select.pack(anchor='w', padx=(20, 0))

      # static frame
      self.static_frame = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.static_frame.pack(side='top', pady=(20, 0), padx=20)
      self.static_frame.pack_propagate(flag=False)

      self.static_text = customtkinter.CTkLabel(self.static_frame, text='Take First Frame of Video')
      self.static_text.pack(anchor='w', padx=(20, 0))

      self.static = customtkinter.CTkCheckBox(self.static_frame, text='Static', checkbox_height=20, checkbox_width=20)
      self.static.pack(anchor='w', padx=(20, 0))

      # fps and padding frame
      self.fps_frame = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.fps_frame.pack(side='top', pady=(20, 0), padx=20)
      self.fps_frame.pack_propagate(flag=False)

      self.fps_text = customtkinter.CTkLabel(self.fps_frame, text='Frames Per Second')
      self.fps_text.pack(anchor='w', padx=(20, 0))

      self.fps_entry = customtkinter.CTkEntry(self.fps_frame, placeholder_text='2')
      self.fps_entry.pack(anchor='w', padx=(20, 0))

      # fps and padding frame
      self.padding_frame = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.padding_frame.pack(side='top', pady=(20, 0), padx=20)
      self.padding_frame.grid_propagate(flag=False)

      self.padding_text = customtkinter.CTkLabel(self.padding_frame, text='Video Padding')
      self.padding_text.grid(row=0, column=0, padx=(20, 0), sticky='w')

      self.padding_entry_text_1 = customtkinter.CTkLabel(self.padding_frame, text='up')
      self.padding_entry_text_1.grid(row=1, column=0, padx=(20, 0), sticky='w')

      self.padding_entry_1 = customtkinter.CTkEntry(self.padding_frame, placeholder_text='0')
      self.padding_entry_1.grid(row=1, column=1, sticky='w')

      self.padding_entry_text_2 = customtkinter.CTkLabel(self.padding_frame, text='down')
      self.padding_entry_text_2.grid(row=1, column=2, padx=(10, 0), sticky='w')

      self.padding_entry_2 = customtkinter.CTkEntry(self.padding_frame, placeholder_text='0')
      self.padding_entry_2.grid(row=1, column=3, sticky='w')

      # self.padding = customtkinter.CTkLabel(self.fps_padding_frame, text='Padding')
      # self.padding.pack(anchor='w', padx=(20, 0))

      # self.padding_entries = customtkinter.CTkFrame(self.fps_padding_frame, width=self.width / 2)
      # self.padding_entries.pack(anchor='w', padx=(20, 0))

      # self.pad_entry_1 = customtkinter.CTkEntry(self.padding_entries, placeholder_text='0')
      # self.pad_entry_1.grid(row=0, column=0)

      # rotate frame
      self.rotate_frame = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.rotate_frame.pack(side='top', pady=(20, 0), padx=20)
      self.rotate_frame.pack_propagate(flag=False)

      self.rotate_text = customtkinter.CTkLabel(self.rotate_frame, text='Rotate the image or video')
      self.rotate_text.pack(anchor='w', padx=(20, 0))

      self.rotate_entry = customtkinter.CTkEntry(self.rotate_frame, placeholder_text='90deg')
      self.rotate_entry.pack(anchor='w', padx=(20, 0))

      # smooth and resize frame
      self.smooth_resize = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.smooth_resize.pack(side='top', pady=(20, 0), padx=20)
      self.smooth_resize.pack_propagate(flag=False)

      # smooth section
      self.smooth_text = customtkinter.CTkLabel(self.smooth_resize, text='Smooth')
      self.smooth_text.pack(anchor='w', padx=(20, 0))

      self.smooth_check = customtkinter.CTkCheckBox(self.smooth_resize, text='Smooth', checkbox_height=20, checkbox_width=20)
      self.smooth_check.pack(anchor='w', padx=(20, 0))

      # resize factor
      self.resize = customtkinter.CTkLabel(self.smooth_resize, text='Resize Factor - Reduce resolution by the factor')
      self.resize.pack(anchor='w', padx=(20, 0))

      self.resize_entry = customtkinter.CTkEntry(self.smooth_resize)
      self.resize_entry.pack(anchor='w', padx=(20, 0))

      # upload frame
      self.upload = customtkinter.CTkFrame(self, width=self.width / 2, height=self.height, fg_color=SECONDARY_COLOR)
      self.upload.pack(side='right', expand=True, padx=(5, 0))
      self.upload.pack_propagate(flag=False)

      # open image or video
      self.file_name_label = customtkinter.CTkLabel(self.upload, text="Display File path here", fg_color=PRIMARY_COLOR, text_color=NEUTRAL_COLOR_1, corner_radius=10, width=self.width / 2)
      self.file_name_label.pack(anchor='w', padx=(20, 20), pady=(10, 0), ipady=10,)

      # Preview label for image or video
      self.preview_label = customtkinter.CTkLabel(self.upload, text="Preview will appear here", text_color=PRIMARY_COLOR, corner_radius=10, width=500, height=200)
      self.preview_label.pack(anchor='w', padx=(20, 20), pady=(20, 0))

      self.open_image_video = customtkinter.CTkButton(self.upload, text='Click to upload image or video', width=self.width / 2, fg_color=PRIMARY_COLOR, hover_color=PRIMARY_COLOR, corner_radius=10, command=self.open_video_image_dialog)
      self.open_image_video.pack(anchor='w', padx=(20, 20), pady=(20, 0), ipady=10)

      # open audio
      self.file_audio_label = customtkinter.CTkLabel(self.upload, text="selected audio path here", fg_color=PRIMARY_COLOR, text_color=NEUTRAL_COLOR_1, corner_radius=10, width=self.width / 2)
      self.file_audio_label.pack(anchor='w', padx=(20, 20), pady=(10, 0), ipady=10,)


      self.open_audio = customtkinter.CTkButton(self.upload, text='Click to upload image or video', width=self.width / 2, fg_color=PRIMARY_COLOR, hover_color=PRIMARY_COLOR, corner_radius=10, command=self.open_audio_dialog)
      self.open_audio.pack(anchor='w', padx=(20, 20), pady=(20, 0), ipady=10)
      

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
    # Determine if the file is an image or video based on its extension
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

# if __name__ == "__main__":
app = App()
app.mainloop()

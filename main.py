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

      self.setting = customtkinter.CTkScrollableFrame(self, width=self.width / 2, height=self.height, fg_color=SECONDARY_COLOR)
      self.setting.pack(side='left', fill='both', expand=True)

      # model frame
      self.model_frame = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.model_frame.pack(side='top', pady=(20, 0), padx=20)
      self.model_frame.grid_propagate(flag=False)

      self.model_text = customtkinter.CTkLabel(self.model_frame, text='Model Version')
      self.model_text.grid(sticky='w', padx=(20, 0), row=0, column=0)

      self.model_select = customtkinter.CTkComboBox(self.model_frame, values=['wav2lip', 'wav2lip_GAN'])
      self.model_select.grid(sticky='w', padx=(20, 0), row=1, column=0)

      self.model_quality_text = customtkinter.CTkLabel(self.model_frame, text='Model Quality')
      self.model_quality_text.grid(sticky='w', padx=(20, 0), row=0, column=1)

      self.model_quality_select = customtkinter.CTkComboBox(self.model_frame, values=['Improved', 'Fast', 'Enhanced'])
      self.model_quality_select.grid(sticky='w', padx=(20, 0), row=1, column=1)

      # static frame
      self.static_frame = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.static_frame.pack(side='top', pady=(20, 0), padx=20)
      self.static_frame.grid_propagate(flag=False)

      self.check_static = customtkinter.BooleanVar(value=False)
      self.static = customtkinter.CTkCheckBox(self.static_frame, text='Static', checkbox_height=20, checkbox_width=20, variable=self.check_static)
      self.static.grid(sticky='w', padx=(20, 0), pady=(20, 0), row=0, column=0)

      self.check_rotate = customtkinter.BooleanVar(value=False)
      self.rotate = customtkinter.CTkCheckBox(self.static_frame, text='Rotate', checkbox_height=20, checkbox_width=20, variable=self.check_rotate)
      self.rotate.grid(sticky='w', padx=(20, 0), pady=(20, 0), row=0, column=1)

      self.check_smooth = customtkinter.BooleanVar(value=False)
      self.smooth = customtkinter.CTkCheckBox(self.static_frame, text='Smooth', checkbox_height=20, checkbox_width=20, variable=self.check_smooth)
      self.smooth.grid(sticky='w', padx=(20, 0), pady=(20, 0), row=0, column=2)

      self.check_res = customtkinter.BooleanVar(value=True)
      self.super_resolution = customtkinter.CTkCheckBox(self.static_frame, text='Super Resolution', checkbox_height=20, checkbox_width=20, variable=self.check_res)
      self.super_resolution.grid(sticky='w', padx=(20, 0), pady=(20, 0), row=0, column=3)

      # padding
      self.padface = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.padface.pack(side='top', pady=(20, 0), padx=20)
      self.padface.grid_propagate(flag=False)

      self.padding_top = customtkinter.CTkLabel(self.padface, text='Padding Top')
      self.padding_top.grid(sticky='w', padx=(20, 0), row=0, column=0)

      self.pad_entry_1 = customtkinter.CTkEntry(self.padface, placeholder_text='0', width=120)
      self.pad_entry_1.grid(sticky='w', padx=(20, 0), row=1, column=0)

      self.padding_bottom = customtkinter.CTkLabel(self.padface, text='Padding Bottom')
      self.padding_bottom.grid(sticky='w', padx=(20, 0), row=0, column=1)

      self.pad_entry_2 = customtkinter.CTkEntry(self.padface, placeholder_text='0', width=120)
      self.pad_entry_2.grid(sticky='w', padx=(20, 0), row=1, column=1)

      self.padding_left = customtkinter.CTkLabel(self.padface, text='Padding Left')
      self.padding_left.grid(sticky='w', padx=(20, 0), row=0, column=3)

      self.pad_entry_3 = customtkinter.CTkEntry(self.padface, placeholder_text='0', width=120)
      self.pad_entry_3.grid(sticky='w', padx=(20, 0), row=1, column=3)

      self.padding_right = customtkinter.CTkLabel(self.padface, text='Padding Right')
      self.padding_right.grid(sticky='w', padx=(20, 0), row=0, column=4)

      self.pad_entry_4 = customtkinter.CTkEntry(self.padface, placeholder_text='0', width=120)
      self.pad_entry_4.grid(sticky='w', padx=(20, 0), row=1, column=4)

      # facemask
      self.facemask = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.facemask.pack(side='top', pady=(20, 0), padx=20)
      self.facemask.grid_propagate(flag=False)

      self.facemask_top = customtkinter.CTkLabel(self.facemask, text='Facemask Top')
      self.facemask_top.grid(sticky='w', padx=(20, 0), row=0, column=0)

      self.face_entry_1 = customtkinter.CTkEntry(self.facemask, placeholder_text='0', width=120)
      self.face_entry_1.grid(sticky='w', padx=(20, 0), row=1, column=0)

      self.facemask_bottom = customtkinter.CTkLabel(self.facemask, text='Facemask Bottom')
      self.facemask_bottom.grid(sticky='w', padx=(20, 0), row=0, column=1)

      self.face_entry_2 = customtkinter.CTkEntry(self.facemask, placeholder_text='0', width=120)
      self.face_entry_2.grid(sticky='w', padx=(20, 0), row=1, column=1)

      self.facemask_left = customtkinter.CTkLabel(self.facemask, text='Facemask Left')
      self.facemask_left.grid(sticky='w', padx=(20, 0), row=0, column=3)

      self.face_entry_3 = customtkinter.CTkEntry(self.facemask, placeholder_text='0', width=120)
      self.face_entry_3.grid(sticky='w', padx=(20, 0), row=1, column=3)

      self.facemask_right = customtkinter.CTkLabel(self.facemask, text='Facemask Right')
      self.facemask_right.grid(sticky='w', padx=(20, 0), row=0, column=4)

      self.face_entry_4 = customtkinter.CTkEntry(self.facemask, placeholder_text='0', width=120)
      self.face_entry_4.grid(sticky='w', padx=(20, 0), row=1, column=4)

      # boundingbox
      self.boundingbox = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.boundingbox.pack(side='top', pady=(20, 0), padx=20)
      self.boundingbox.grid_propagate(flag=False)

      self.bounding_top = customtkinter.CTkLabel(self.boundingbox, text='Bounding Top')
      self.bounding_top.grid(sticky='w', padx=(20, 0), row=0, column=0)

      self.bound_entry_1 = customtkinter.CTkEntry(self.boundingbox, placeholder_text='0', width=120)
      self.bound_entry_1.grid(sticky='w', padx=(20, 0), row=1, column=0)

      self.bounding_bottom = customtkinter.CTkLabel(self.boundingbox, text='Bounding Bottom')
      self.bounding_bottom.grid(sticky='w', padx=(20, 0), row=0, column=1)

      self.bound_entry_2 = customtkinter.CTkEntry(self.boundingbox, placeholder_text='0', width=120)
      self.bound_entry_2.grid(sticky='w', padx=(20, 0), row=1, column=1)

      self.bounding_left = customtkinter.CTkLabel(self.boundingbox, text='Bounding Left')
      self.bounding_left.grid(sticky='w', padx=(20, 0), row=0, column=3)

      self.bound_entry_3 = customtkinter.CTkEntry(self.boundingbox, placeholder_text='0', width=120)
      self.bound_entry_3.grid(sticky='w', padx=(20, 0), row=1, column=3)

      self.bounding_right = customtkinter.CTkLabel(self.boundingbox, text='Bounding Right')
      self.bounding_right.grid(sticky='w', padx=(20, 0), row=0, column=4)

      self.bound_entry_4 = customtkinter.CTkEntry(self.boundingbox, placeholder_text='0', width=120)
      self.bound_entry_4.grid(sticky='w', padx=(20, 0), row=1, column=4)

      # crop
      self.crop = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.crop.pack(side='top', pady=(20, 0), padx=20)
      self.crop.grid_propagate(flag=False)

      self.crop_top = customtkinter.CTkLabel(self.crop, text='Crop Top')
      self.crop_top.grid(sticky='w', padx=(20, 0), row=0, column=0)

      self.crop_entry_1 = customtkinter.CTkEntry(self.crop, placeholder_text='0', width=120)
      self.crop_entry_1.grid(sticky='w', padx=(20, 0), row=1, column=0)

      self.crop_bottom = customtkinter.CTkLabel(self.crop, text='Crop Bottom')
      self.crop_bottom.grid(sticky='w', padx=(20, 0), row=0, column=1)

      self.crop_entry_2 = customtkinter.CTkEntry(self.crop, placeholder_text='0', width=120)
      self.crop_entry_2.grid(sticky='w', padx=(20, 0), row=1, column=1)

      self.crop_left = customtkinter.CTkLabel(self.crop, text='Crop Left')
      self.crop_left.grid(sticky='w', padx=(20, 0), row=0, column=3)

      self.crop_entry_3 = customtkinter.CTkEntry(self.crop, placeholder_text='0', width=120)
      self.crop_entry_3.grid(sticky='w', padx=(20, 0), row=1, column=3)

      self.crop_right = customtkinter.CTkLabel(self.crop, text='Crop Right')
      self.crop_right.grid(sticky='w', padx=(20, 0), row=0, column=4)

      self.crop_entry_4 = customtkinter.CTkEntry(self.crop, placeholder_text='0', width=120)
      self.crop_entry_4.grid(sticky='w', padx=(20, 0), row=1, column=4)

      # output, upscaler, frames-per-sec
      self.output_up_frame = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.output_up_frame.pack(side='top', pady=(20, 0), padx=20)
      self.output_up_frame.grid_propagate(flag=False)

      self.output_height_text = customtkinter.CTkLabel(self.output_up_frame, text='Output Height')
      self.output_height_text.grid(sticky='w', padx=(20, 0), row=0, column=0)

      self.output_height = customtkinter.CTkComboBox(self.output_up_frame, values=['full resolution', 'half resolution'])
      self.output_height.grid(sticky='w', padx=(20, 0), row=1, column=0)

      self.upscaler_text = customtkinter.CTkLabel(self.output_up_frame, text='Upscaler')
      self.upscaler_text.grid(sticky='w', padx=(20, 0), row=0, column=1)

      self.upscaler = customtkinter.CTkComboBox(self.output_up_frame, values=['gfpgan', 'Restoreformer'])
      self.upscaler.grid(sticky='w', padx=(20, 0), row=1, column=1)
      
      self.fps_text = customtkinter.CTkLabel(self.output_up_frame, text='Frames Per Second')
      self.fps_text.grid(sticky='w', padx=(20, 0), row=0, column=2)

      self.frames_per_second = customtkinter.CTkEntry(self.output_up_frame)
      self.frames_per_second.insert(0, '25')
      self.frames_per_second.grid(sticky='w', padx=(20, 0), row=1, column=2)

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

      self.submit_btn = customtkinter.CTkButton(self.upload, text='Sync Video', width=self.width / 2, fg_color=PRIMARY_COLOR, hover_color=PRIMARY_COLOR, corner_radius=10, command=self.invoke)
      self.submit_btn.pack(anchor='w', padx=(20, 20), pady=(20, 0), ipady=10)
      

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
      version = self.model_select.get()
      quality = self.model_quality_select.get()
      static = self.check_static.get()
      rotate = self.check_rotate.get()
      smooth = self.check_smooth.get()
      super_resolution =self.check_res.get()

      padding = {'top': self.pad_entry_1.get(), 'bottom': self.pad_entry_2.get(), 'left': self.pad_entry_3.get(), 'right': self.pad_entry_4.get()}
      box = {'top': self.bound_entry_1.get(), 'bottom': self.bound_entry_2.get(), 'left': self.bound_entry_3.get(), 'right': self.bound_entry_4.get()}
      crop = {'top': self.crop_entry_1.get(), 'bottom': self.crop_entry_2.get(), 'left': self.crop_entry_3.get(), 'right': self.crop_entry_4.get()}
      upscaler = self.upscaler.get()
      frames_per_second = self.frames_per_second.get()

      face = self.file_name_label.cget('text').replace('Selected: ', '')
      audio = self.file_audio_label.cget('text')

      print(version, quality, static, rotate, smooth, super_resolution, padding, box, crop, upscaler, frames_per_second)
      print(face, audio)

# if __name__ == "__main__":
app = App()
app.mainloop()
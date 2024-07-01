import customtkinter
from settingvalue import get_settings
from color import *

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
      self.pad_entry_1.insert(0, '0')
      self.pad_entry_1.grid(sticky='w', padx=(20, 0), row=1, column=0)

      self.padding_bottom = customtkinter.CTkLabel(self.padface, text='Padding Bottom')
      self.padding_bottom.grid(sticky='w', padx=(20, 0), row=0, column=1)

      self.pad_entry_2 = customtkinter.CTkEntry(self.padface, placeholder_text='0', width=120)
      self.pad_entry_2.insert(0, '0')
      self.pad_entry_2.grid(sticky='w', padx=(20, 0), row=1, column=1)

      self.padding_left = customtkinter.CTkLabel(self.padface, text='Padding Left')
      self.padding_left.grid(sticky='w', padx=(20, 0), row=0, column=3)

      self.pad_entry_3 = customtkinter.CTkEntry(self.padface, placeholder_text='0', width=120)
      self.pad_entry_3.insert(0, '0')
      self.pad_entry_3.grid(sticky='w', padx=(20, 0), row=1, column=3)

      self.padding_right = customtkinter.CTkLabel(self.padface, text='Padding Right')
      self.padding_right.grid(sticky='w', padx=(20, 0), row=0, column=4)

      self.pad_entry_4 = customtkinter.CTkEntry(self.padface, placeholder_text='0', width=120)
      self.pad_entry_4.insert(0, '0')
      self.pad_entry_4.grid(sticky='w', padx=(20, 0), row=1, column=4)

      # facemask
      self.facemask = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.facemask.pack(side='top', pady=(20, 0), padx=20)
      self.facemask.grid_propagate(flag=False)

      self.facemask_top = customtkinter.CTkLabel(self.facemask, text='Size')
      self.facemask_top.grid(sticky='w', padx=(20, 0), row=0, column=0)

      self.face_entry_1 = customtkinter.CTkEntry(self.facemask, placeholder_text='0', width=120)
      self.face_entry_1.insert(0, '2.5')
      self.face_entry_1.grid(sticky='w', padx=(20, 0), row=1, column=0)

      self.facemask_bottom = customtkinter.CTkLabel(self.facemask, text='Feathering')
      self.facemask_bottom.grid(sticky='w', padx=(20, 0), row=0, column=1)

      self.face_entry_2 = customtkinter.CTkEntry(self.facemask, placeholder_text='0', width=120)
      self.face_entry_2.insert(0, '2')
      self.face_entry_2.grid(sticky='w', padx=(20, 0), row=1, column=1)

      self.facemask_left = customtkinter.CTkLabel(self.facemask, text='Mouth Tracking')
      self.facemask_left.grid(sticky='w', padx=(20, 0), row=0, column=3)

      self.face_entry_3 = customtkinter.CTkComboBox(self.facemask, values=['True', 'False'])
      self.face_entry_3.grid(sticky='w', padx=(20, 0), row=1, column=3)

      self.facemask_right = customtkinter.CTkLabel(self.facemask, text='Debug Mask')
      self.facemask_right.grid(sticky='w', padx=(20, 0), row=0, column=4)

      self.face_entry_4 = customtkinter.CTkComboBox(self.facemask, values=['True', 'False'], width=120)
      self.face_entry_4.grid(sticky='w', padx=(20, 0), row=1, column=4)

      # boundingbox
      self.boundingbox = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.boundingbox.pack(side='top', pady=(20, 0), padx=20)
      self.boundingbox.grid_propagate(flag=False)

      self.bounding_top = customtkinter.CTkLabel(self.boundingbox, text='Bounding Top')
      self.bounding_top.grid(sticky='w', padx=(20, 0), row=0, column=0)

      self.bound_entry_1 = customtkinter.CTkEntry(self.boundingbox, placeholder_text='0', width=120)
      self.bound_entry_1.insert(0, '-1')
      self.bound_entry_1.grid(sticky='w', padx=(20, 0), row=1, column=0)

      self.bounding_bottom = customtkinter.CTkLabel(self.boundingbox, text='Bounding Bottom')
      self.bounding_bottom.grid(sticky='w', padx=(20, 0), row=0, column=1)

      self.bound_entry_2 = customtkinter.CTkEntry(self.boundingbox, placeholder_text='0', width=120)
      self.bound_entry_2.insert(0, '-1')
      self.bound_entry_2.grid(sticky='w', padx=(20, 0), row=1, column=1)

      self.bounding_left = customtkinter.CTkLabel(self.boundingbox, text='Bounding Left')
      self.bounding_left.grid(sticky='w', padx=(20, 0), row=0, column=3)

      self.bound_entry_3 = customtkinter.CTkEntry(self.boundingbox, placeholder_text='0', width=120)
      self.bound_entry_3.insert(0, '-1')
      self.bound_entry_3.grid(sticky='w', padx=(20, 0), row=1, column=3)

      self.bounding_right = customtkinter.CTkLabel(self.boundingbox, text='Bounding Right')
      self.bounding_right.grid(sticky='w', padx=(20, 0), row=0, column=4)

      self.bound_entry_4 = customtkinter.CTkEntry(self.boundingbox, placeholder_text='0', width=120)
      self.bound_entry_4.insert(0, '-1')
      self.bound_entry_4.grid(sticky='w', padx=(20, 0), row=1, column=4)

      # crop
      self.crop = customtkinter.CTkFrame(self.setting, width=self.width / 2, height=80, fg_color=PRIMARY_COLOR)
      self.crop.pack(side='top', pady=(20, 0), padx=20)
      self.crop.grid_propagate(flag=False)

      self.crop_top = customtkinter.CTkLabel(self.crop, text='Crop Top')
      self.crop_top.grid(sticky='w', padx=(20, 0), row=0, column=0)

      self.crop_entry_1 = customtkinter.CTkEntry(self.crop, placeholder_text='0', width=120)
      self.crop_entry_1.insert(0, '0')
      self.crop_entry_1.grid(sticky='w', padx=(20, 0), row=1, column=0)

      self.crop_bottom = customtkinter.CTkLabel(self.crop, text='Crop Bottom')
      self.crop_bottom.grid(sticky='w', padx=(20, 0), row=0, column=1)

      self.crop_entry_2 = customtkinter.CTkEntry(self.crop, placeholder_text='0', width=120)
      self.crop_entry_2.insert(0, '-1')
      self.crop_entry_2.grid(sticky='w', padx=(20, 0), row=1, column=1)

      self.crop_left = customtkinter.CTkLabel(self.crop, text='Crop Left')
      self.crop_left.grid(sticky='w', padx=(20, 0), row=0, column=3)

      self.crop_entry_3 = customtkinter.CTkEntry(self.crop, placeholder_text='0', width=120)
      self.crop_entry_3.insert(0, '0')
      self.crop_entry_3.grid(sticky='w', padx=(20, 0), row=1, column=3)

      self.crop_right = customtkinter.CTkLabel(self.crop, text='Crop Right')
      self.crop_right.grid(sticky='w', padx=(20, 0), row=0, column=4)

      self.crop_entry_4 = customtkinter.CTkEntry(self.crop, placeholder_text='0', width=120)
      self.crop_entry_4.insert(0, '-1')
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

      self.submit_btn = customtkinter.CTkButton(self.upload, text='Sync Video', width=self.width / 2, fg_color=PRIMARY_COLOR, hover_color=PRIMARY_COLOR, corner_radius=10, command=lambda : get_settings(self))
      self.submit_btn.pack(anchor='w', padx=(20, 20), pady=(20, 0), ipady=10)
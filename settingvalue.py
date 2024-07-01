from time import sleep
from validate_values import validate_values

def get_settings(self):
      # validate values first before accepting and processing
      validate_values(self=self)

      version = self.model_select.get()
      quality = self.model_quality_select.get()
      static = self.check_static.get()
      rotate = self.check_rotate.get()
      smooth = self.check_smooth.get()
      super_resolution =self.check_res.get()

      padding = {'top': self.pad_1, 'bottom': self.pad_2, 'left': self.pad_3, 'right': self.pad_4}

      box = {'top': self.bound_1, 'bottom': self.bound_2, 'left': self.bound_3, 'right': self.bound_4}

      crop = {'top': self.crop_1, 'bottom': self.crop_2, 'left': self.crop_3, 'right': self.crop_4}

      if (self.face_entry_3.get() == 'True'): mouth_tracking = True 
      else: mouth_tracking = False

      if (self.face_entry_4.get() == 'True'): debug_mask = True 
      else: debug_mask = False

      face_mask = {'size': self.face_1, 'feathering': self.face_2, 'mouth_tracking': mouth_tracking, 'debug_mask': debug_mask}

      upscaler = self.upscaler.get()

      frames_per_second = self.frames_per_second.get()

      face = self.file_name_label.cget('text').replace('Selected: ', '')
      audio = self.file_audio_label.cget('text')

      # go to default
      self.submit_btn.configure(text='')
      self.submit_btn.configure(text='Loading...')
      sleep(4.0)

      self.setting.pack_forget()
      self.upload.pack_forget()

      self.history_parent_frame.pack(side='top', fill='both', expand=True)

      print(version, quality, static, rotate, smooth, super_resolution, padding, box, crop, upscaler, frames_per_second, face, audio, face_mask)
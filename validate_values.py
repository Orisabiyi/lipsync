def validate_values(self):
    try:
        # padding
        self.pad_1 = int(self.pad_entry_1.get())
        self.pad_2 = int(self.pad_entry_2.get())
        self.pad_3 = int(self.pad_entry_3.get())
        self.pad_4 = int(self.pad_entry_4.get())

        # face_mask
        self.face_1 = float(self.face_entry_1.get())
        self.face_2 = int(self.face_entry_2.get())

        # bounding
        self.bound_1 = int(self.bound_entry_1.get())
        self.bound_2 = int(self.bound_entry_2.get())
        self.bound_3 = int(self.bound_entry_3.get())
        self.bound_4 = int(self.bound_entry_4.get())

        # crop
        self.crop_1 = int(self.crop_entry_1.get())
        self.crop_2 = int(self.crop_entry_2.get())
        self.crop_3 = int(self.crop_entry_3.get())
        self.crop_4 = int(self.crop_entry_4.get())
       
    except ValueError:
        pad_1_len = len(self.pad_entry_1.get())
        pad_2_len = len(self.pad_entry_2.get())
        pad_3_len = len(self.pad_entry_3.get())
        pad_4_len = len(self.pad_entry_4.get())

        face_1_len = len(self.face_entry_1.get())
        face_2_len = len(self.face_entry_2.get())

        bound_1_len = len(self.bound_entry_1.get())
        bound_2_len = len(self.bound_entry_2.get())
        bound_3_len = len(self.bound_entry_3.get())
        bound_4_len = len(self.bound_entry_4.get())

        crop_1_len = len(self.crop_entry_1.get())
        crop_2_len = len(self.crop_entry_2.get())
        crop_3_len = len(self.crop_entry_3.get())
        crop_4_len = len(self.crop_entry_4.get())

        # pad reset values
        self.pad_entry_1.delete(0, pad_1_len)
        self.pad_entry_1.insert(0, '0')

        self.pad_entry_2.delete(0, pad_2_len)
        self.pad_entry_2.insert(0, '0')

        self.pad_entry_3.delete(0, pad_3_len)
        self.pad_entry_3.insert(0, '0')

        self.pad_entry_4.delete(0, pad_4_len)
        self.pad_entry_4.insert(0, '0')

        # face reset
        self.face_entry_1.delete(0, face_1_len)
        self.face_entry_1.insert(0, '2.5')

        # bound reset
        self.face_entry_2.delete(0, face_2_len)
        self.face_entry_2.insert(0, '2')

        self.bound_entry_1.delete(0, bound_1_len)
        self.bound_entry_1.insert(0, '-1')

        self.bound_entry_2.delete(0, bound_2_len)
        self.bound_entry_1.insert(0, '-1')

        self.bound_entry_3.delete(0, bound_3_len)
        self.bound_entry_1.insert(0, '-1')

        self.bound_entry_4.delete(0, bound_4_len)
        self.bound_entry_1.insert(0, '-1')

        # crop reset
        self.crop_entry_1.delete(0, crop_1_len)
        self.crop_entry_1.insert(0, '-1')

        self.crop_entry_2.delete(0, crop_2_len)
        self.crop_entry_2.insert(0, '-1')

        self.crop_entry_3.delete(0, crop_3_len)
        self.crop_entry_3.insert(0, '-1')

        self.crop_entry_4.delete(0, crop_4_len)
        self.crop_entry_4.insert(0, '-1')
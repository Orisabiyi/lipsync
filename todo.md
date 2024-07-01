model: wav2lip, wav2lip-gan
static - take the first frame of the video and use for generation
frames per second - number
padding [up, down, left, right] = [0, 10, 0, 0]
box [up, down, left, right] = [-1, -1, -1, -1]
rotate - rotates the image/video 90deg
smooth = checkbox
resize factor - reduce resolution by the factor (number)

###########

- model_select - combobox
- model_quality_select - combobox
- check_static/static - checkbox
- check_rotate/rotate - checkbox
- check_smooth/smooth - checkbox
- check_res/super_resolution - checkbox
- pad_entry_1
- pad_entry_2
- pad_entry_3
- pad_entry_4

/_Coming to the face_/

- face_entry_1
- face_entry_2
- face_entry_3
- face_entry_4

- bound_entry_1
- bound_entry_2
- bound_entry_3
- bound_entry_4

- crop_entry_1
- crop_entry_2
- crop_entry_3
- crop_entry_4

- output_height - combobox
- upscaler - combobox
- frames_per_second - combobox
  -file_name_label - label
- preview_label - lable
- file_audio_label

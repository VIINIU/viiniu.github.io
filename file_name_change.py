import os

base_path =  "C:\\Users\\Seeroo\\Downloads\\AM"

for current_num in range(18,51):
    current_file_path = os.path.join(base_path, f"{current_num}.jpg")
    new_file_path = os.path.join(base_path, f"AM{current_num}.jpg")
    os.rename(current_file_path, new_file_path)
import os
import shutil

path = "C:/Users/Admin/Downloads"

files = os.listdir(path)

for file in files:

    if os.path.isdir(os.path.join(path, file)):
        continue

    if file.endswith(".jpg") or file.endswith(".png"):
        folder = "Images"

    elif file.endswith(".pdf") or file.endswith(".docx"):
        folder = "Documents"

    elif file.endswith(".mp4"):
        folder = "Videos"

    else:
        folder = "Others"

    folder_path = os.path.join(path, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

print("Files organized successfully!")
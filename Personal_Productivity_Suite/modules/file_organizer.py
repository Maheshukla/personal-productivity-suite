import os
import shutil

def organize():
    path = input("Enter folder path: ")

    if not os.path.exists(path):
        print("Folder not found")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = file.split(".")[-1]

            folder = os.path.join(path, ext)

            if not os.path.exists(folder):
                os.makedirs(folder)

            shutil.move(file_path, os.path.join(folder, file))

    print("Files organized")
# Write a script to move all .csv files from one folder to another.

import os
import shutil

path = "/home/ravi/Downloads/Data_eng_workspace/Data_Engineering/BASICPYTHON_FOR_DATA_ENG"

def list_of_all_files(path):

    if os.path.exists(path):
        files = os.listdir(path)

    return files

def move_files():
    dest_folder = os.path.join(path,'allcsvfiles')
    if not os.path.exists(dest_folder):
        os.makedirs("allcsvfiles")

    for file in list_of_all_files(path):

        sour_path = os.path.join(path,file)
        dest_path = os.path.join(dest_folder,file)

        if os.path.isfile(sour_path) and  file.endswith(".csv"):
            shutil.move(sour_path,dest_path)
            print(f'moved file {file}')

if __name__ == "__main__":
    move_files()
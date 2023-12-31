#TODO for a given folder list only regular files and sum the size of all

import os.path

my_folder = '../learning_material'

files_list = [file for file in os.listdir(my_folder) if os.path.isfile(os.path.join(my_folder, file))]

def folder_size(folder):
    total_size = 0

    for f in os.listdir(folder):
        file_path = os.path.join(folder, f)

        if os.path.isfile(file_path):
            total_size += os.path.getsize(file_path)

        elif os.path.isdir(file_path):
            total_size += folder_size(file_path)

    return total_size


print(f'Total size of all files in the folder is {folder_size(my_folder)}.')



# print(os.listdir(my_folder))
# a = sum(os.path.getsize(os.path.join(my_folder, f))
#         for f in os.listdir(my_folder) if os.path.isfile(os.path.join(my_folder, f)))

# def folder_size(folder):
#     a = sum(os.path.getsize(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)))
#     return a

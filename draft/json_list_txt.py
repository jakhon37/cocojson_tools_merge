"""
store json files' name and path in folder to txt file

"""



import os
import shutil

# path = r'C:/Users/jakho/PROJECTS/label/data/testData/'
# path = r'C:/Users/jakho/PROJECTS/label/data_new/testData/val/'
# path = './data_new/testData/val/'
path = './data_new/testData/train/'


# C:\Users\jakho\PROJECTS\label
FileList = []

# extensions = ['.pdf', '.docx', '.jpeg', '.json']
extensions = ['.json']


# Scanning For Files :-

with os.scandir(path) as DirList:
    for root, dirs_list, files_list in os.walk(path):
        for file_name in files_list:
            # this loops over each extensions and evaluates it
            for extension in extensions:
                if os.path.splitext(file_name)[-1] == extension:
                    ll = (" -r ./data_new/testData/train/ -j ./data_new/testData/train")
                    file_name_path = os.path.join(ll , file_name)
                    print(f'file_name_path --- {file_name_path}')
                    FileList.append(file_name_path)
                    with open("found_file_1.txt", 'w') as ffile:
                        for fname in FileList:
                            ffile.write(fname)


"""
import shutil

path = 'C:'
FileList = []

extensions = ['.pdf', '.docx', '.jpeg']

# Scanning For Files :-

with os.scandir(path) as DirList:
    for root, dirs_list, files_list in os.walk(path):
        for file_name in files_list:
            # this loops over each extensions and evaluates it
            for extension in extensions:
                if os.path.splitext(file_name)[-1] == extension:
                    file_name_path = os.path.join(root, file_name)
                    # break here so that if matching extension is found it stops checking
                    break
    for files in DirList:
        if files.is_file():
            FileList.append(files.name)

# After that it iterates over the FileList and write names to text file
with open("found_file.txt", 'w') as ffile:
    for fname in files_list:
        ffile.write(fname)
#copies all files into a folder called found_files
newPath = shutil.copy('files_list', 'C:/Users/PacY/Downloads/found_files') 
"""
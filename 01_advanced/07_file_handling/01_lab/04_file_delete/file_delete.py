import os

path = os.path.join("../03_file_writer/my_first_file.txt")

if os.path.isfile(path):
    os.remove(path)
else:
    print("File already deleted!")

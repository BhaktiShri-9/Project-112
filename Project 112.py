import os
import shutil

source = "C:/Users/Admin/Downloads"
destination = "C:/Users/Admin/Desktop"

list = os.listdir(source)

for i in list:
    name, extension = os.path.splitext(i)
    if extension == " ":
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + i
        path2 = destination +'/' + "documents"
        path3 = destination + '/' + "documents" + '/' + i

        if os.path.exists(path2):
            print("Moving" + i)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving" + i)
            shutil.move(path1, path3)
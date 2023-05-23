import os
import shutil

from_dir = "C:/Users/USER/Downloads"
to_dir = "C:/Users/USER/Desktop/Document_Files"

list_of_files = os.listdr(from_dir)
print(list_of_files)

for fl_na in list_of_files:

    name, extension = os.path.splitext(fl_na)
    
    if extension == '':
        continue
    if extension in ['.txt, .doc, .docx, .pdf']:

        path1 = from_dir + '/' + fl_na                       
        path2 = to_dir + '/' + "Pdf_Files"                    
        path3 = to_dir + '/' + "Pdf_Files" + '/' + fl_na   
        
        if os.path.exists(path2):
          print("Moving " + fl_na + ".....")

          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + fl_na + ".....")
          shutil.move(path1, path3)

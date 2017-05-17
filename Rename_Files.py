import os
def rename_files():
    #get the files
    file_list = os.listdir("E:\Udacity\Python learning\prank")

    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir("E:\Udacity\Python learning\prank")

    for file_name in file_list:
        print("Old Name -" + file_name)
        print("New name -"+ file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir(saved_path)

rename_files()

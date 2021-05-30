# this project will automatically delete the temp files which are stored on your pc
import os
import shutil

path = "C:\Windows\Temp"

print("Cleaning the data")
print("Cleaning the data.")
print("Cleaning the data..")
print("Cleaning the data...")
print("Cleaning the data")
print("Cleaning the data.")
print("Cleaning the data..")
print("Cleaning the data...")
print("Cleaning the data")
print("Cleaning the data.")
print("Cleaning the data..")
print("Cleaning the data...")
print("Cleaning the data")
print("Cleaning the data.")
print("Cleaning the data..")




for root_folder, folders, files in os.walk(path):
    for i in folders:
        shutil.rmtree(root_folder + '/'+ i)
        print(i)
    for f in files:
        os.remove(root_folder + '/' + f)

print("Your pc is now clean")

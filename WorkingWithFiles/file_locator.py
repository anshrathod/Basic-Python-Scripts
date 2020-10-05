import os
import os.path

file_name = input("File name : ")  # Target File
target_dir = input("Directory to be searched : ") # Target Directory

#file_list = os.listdir(target_dir)

file_exists = False
for dirpath, dirnames, filenames in os.walk(target_dir):
	if file_name in filenames:
		print ("File exists at : ", os.path.join(dirpath, file_name))
		file_exists = True
		break

if not file_exists:
	print ("File does not exist in directory")

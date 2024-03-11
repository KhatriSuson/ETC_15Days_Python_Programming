import os

working_directory = os.getcwd()
print("My current working directory = ", working_directory)

files = os.listdir(working_directory)  # List all files and

print(files)


os_name = os.name
print("my operating system =", os_name)


os.system("ping www.github.com")
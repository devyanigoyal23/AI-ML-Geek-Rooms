#Write a program to print the contents of a directory using the os module.

import os

# Define the directory path ('.' refers to the current directory)
directory_path = "/AI-ML-Geek-Rooms"

try:
    # Get the list of all files and directories
    contents = os.listdir(directory_path)

    print(f"Contents of '{os.path.abspath(directory_path)}':\n")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")
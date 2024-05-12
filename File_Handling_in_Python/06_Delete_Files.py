# HOW TO DELETE FILES 
    # To remove a file using Python, you need to import a module called os which contains functions that interact with your operating system.
    # 💡 Tip: A module is a Python file with related variables, functions, and classes.
    # Particularly, you need the remove() function. This function takes the path to the file as argument and deletes the file automatically.
import os

filename = "sample.txt"
if os.path.exists(filename):#check if the filenane exists
    os.remove(filename) #delete filename
    print(f"{filename} has been deleted successfuly.")
else:
    print(f"{filename} doesn't exist.")
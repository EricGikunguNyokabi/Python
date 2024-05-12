# OPEN FILE FOR MULTIPLE APPLICATIONS
    # If you open a file in "r" mode (read), and then try to write to it:
# with open("languages.txt","r") as file:
#     file.write("Multiple Applications")
    # UnsupportedOperation: not writable
    # The same will occur with the "a" (append) mode.
    # How can we solve this? To be able to read a file and perform another operation in the same program, you need to add the "+" symbol to the mode, like this:
with open("file1.txt","r+") as file:
    content = file.read() #read the content of the file
    file.write("\n\tDjango : Is a little more complex than Flask but its the best for getting job done.") #write to the file
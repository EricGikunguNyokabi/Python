# HOW TO WRITE INTO A FILE
    # Write
        # To modify (write to) a file, you need to use the write() method. You have two ways to do it (append or write) based on the mode that you choose to open it with. Let's see them in detail.
            # file_object = open(filename, mode)
            # file_object = write(new_content)
            # file_object.close()

file_object = open("file1.txt","w")
file_object.write("I am Learning Python")
file_object.close()
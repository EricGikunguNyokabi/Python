# HOW TO CREATE A FILE
    # If you need to create a file "dynamically" using Python, you can do it with the "x" mode.
    # Create
            # file_object = open(filename, mode)
            # file_object.close()
file_object = open("file1.txt", "x")
file_object.close()

# HOW TO MODIFY A FILE
# Append
        # "Appending" means adding something to the end of another thing. The "a" mode allows you to open a file to append some content to it.
        # we can open it using the "a" mode (append) and then, call the write() method, passing the content that we want to append as argument.
            # file_object = open(filename, mode)
            # file_object = write(new_content)
            # file_object.close()
file_object = open("file1.txt", "a")
file_object.write("\nPython has Frameworks such as Django and Flask. I love Django.")
file_object.close()
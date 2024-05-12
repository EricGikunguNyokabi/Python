# read files
with open("file.txt","r+") as f:
    print(f.readlines())


# Trying to Read it Again
    # After the body has been completed, the file is automatically closed, so it can't be read without opening it again. But wait! We have a line that tries to read it again, right here below:
print(f.readlines())
# ValueError: I/O operation on closed file.
    # This error is thrown because we are trying to read a closed file. Awesome, right? The context manager does all the heavy work for us, it is readable, and concise.
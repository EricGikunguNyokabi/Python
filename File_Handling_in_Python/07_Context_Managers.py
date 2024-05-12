# CONTEXT MANAGERS 
    # Context Managers are Python constructs that will make your life much easier. By using them, you don't need to remember to close a file at the end of your program and you have access to the file in the particular part of the program that you choose.

    # MyContextManager class defines the __enter__() and __exit__() methods to be used as context managers.
    # The __enter__() method is called when the with the block is entered, and the __exit__() method is called when the block is exited, either normally or due to an exception.
    # When an exception occurs inside the block, the __exit__() method is called with the exception type, value, and traceback as arguments. If the __exit__() method returns True, the exception is considered handled and the program continues. If it returns False or raises another exception, the original exception is propagated.
class MyContextManager: 
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        if exc_type is not None:
            print(f"An error of type {exc_type} occured: {exc_val}")
            return True
        
with MyContextManager() as cm:
    print("Inside context")
    
# This context manager opens the languages.txt file for read/write operations and assigns that file object to the variable f. This variable is used in the body of the context manager to refer to the file object.
with open("file1.txt","r+") as f:
    print(f.readlines())
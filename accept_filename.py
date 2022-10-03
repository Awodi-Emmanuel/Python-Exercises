import pathlib

def accept_filename():
    f = input("Enter your file name: ")

    # function to return the file extension
    file_extension = pathlib.Path(f).suffix
    print("File Extension: ", file_extension)



accept_filename()
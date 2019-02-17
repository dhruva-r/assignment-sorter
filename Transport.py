import os
import SearchFileString


def create_folder(directory, key):
    try:
        if not os.path.exists(directory + "/" + key):
            os.makedirs(directory + "/" + key)
        else:
            print("suhfis")
    except OSError:
        print('Error: Creating directory. ' + directory)

# Creates a folder in the current directory called data


def trans(directory, path, key):

    print(path)
    print(directory + key + "/" + SearchFileString.returnfilename(path))
    os.rename(path, directory + "/" + key + "/" + SearchFileString.returnfilename(path))

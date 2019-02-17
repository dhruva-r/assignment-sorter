import os
import SearchFileString




def create_folder(directory, key):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory + "\\" + key)
    except OSError:
        print('Error: Creating directory. ' + directory)

# Creates a folder in the current directory called data


def trans(directory, path, key):

    os.rename(path, directory + key + "/" + SearchFileString.returnfilename(path))

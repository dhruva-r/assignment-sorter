import os
import ntpath

input_dir = "C:/"


def create_folder(directory, key):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory + "\\" + key)
    except OSError:
        print('Error: Creating directory. ' + directory)

# Creates a folder in the current directory called data


def trans(path, key):

    head2, tail2 = ntpath.split(path)
    os.rename(path, input_dir + key + "/" + tail2)



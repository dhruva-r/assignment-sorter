import os
import ntpath

input_dir = "tttttt"


def create_folder(directory, key):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory + "/" + key)
    except OSError:
        print('Error: Creating directory. ' + directory)

# Creates a folder in the current directory called data


def trans(path, key):

    head1, tail2 = ntpath.split(path)
    os.rename(path, input_dir + key + tail2)

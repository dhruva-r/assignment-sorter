import tkinter
import tkinter.filedialog
import ntpath
import os


def search(fname, kword):
    # this function just checks the filename for the keyword, returns true if it is there, false if not
    if fname.find(kword) != -1:
        return True
    return False


def returnfilename(filepath):
    # this function takes the filepath and returns the filename
    head, tail = ntpath.split(filepath)
    return tail


def sortfolder(filenames, keyword, directory):
    length = (len(filenames))
    # this keyword will be set based on the input of the user on what to search

    for x in range(length):
        filepath = filenames[x]
        filename = returnfilename(filepath)
        if search(filename, keyword):
            create_folder(directory, keyword)
            print(directory)
            trans(directory, filepath, keyword)


def create_folder(directory, key):
    # This function checks if a dir exists if not, throws error and prints to console, if it does creates folder
    try:
        if not os.path.exists(directory + "/" + key):
            os.makedirs(directory + "/" + key)
        else:
            print("Folder Already Exists")
    except OSError:
        print('Error: Creating directory. ' + directory)

# Creates a folder in the current directory called data


def trans(directory, path, key):
    # this function transports the files by renaming the file
    print(path)
    print(directory + key + "/" + returnfilename(path))
    os.rename(path, directory + "/" + key + "/" + returnfilename(path))


i = 0
keywords = []


def grab_keywords(k):

    keywords.append(k)


def main():
    # this returns a tuple based on the selected files of the user
    filenames = tkinter.filedialog.askopenfilenames()
    keywords.append(".")
    directory = "C:/Users/dhruv/Documents"
    for x in range(len(keywords)):
        keyword = keywords[x]
        sortfolder(filenames, keyword, directory)


if __name__ == "__main__":
    main()



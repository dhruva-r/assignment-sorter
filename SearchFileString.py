import tkinter
import tkinter.filedialog
import ntpath

def search(fname, kword):
    # this function just checks the filename for the keyword, returns true if it is there, false if not
    if fname.find(kword) != -1:
        return True
    return False

def returnfilename(filepath):
    # this function takes the filepath and returns the filename
    head, tail = ntpath.split(filepath)
    return tail

def main():
    # this returns a tuple based on the selected files of the user
    filename = tkinter.filedialog.askopenfilenames()
    length = (len(filename))
    # this keyword will be set based on the input of the user on what to search
    keyword = "key"

    for x in range (length):
        filepath = filename[x]
        filename = returnfilename(filepath)
        if search(filename, keyword) == True:
            # this is where you would transfer the file to folder filename
        else:
            # this is where you would move the file to other folder

if __name__ == "__main__":
    main()



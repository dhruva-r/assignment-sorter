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

# this returns a tuple based on the selected files of the user
filename = tkinter.filedialog.askopenfilenames()






length = (len(filename))
file = filename[0]
returnfilename(file)




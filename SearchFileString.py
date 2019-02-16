import tkinter
import tkinter.filedialog
import ntpath

filename = tkinter.filedialog.askopenfilenames()
print(filename)
print(len(filename))
tail = filename[0]
print(tail)
head, tail = ntpath.split(filename[0])
print(head)
print(tail)
# this function just checks the filename for the keyword, returns true if it is there, false if not


def search(fname, kword):
    if fname.find(kword) != -1:
        return True
    return False


def returnfilename(fPath):

    return ""

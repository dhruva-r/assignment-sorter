import tkinter
import tkinter.filedialog

filename = tkinter.filedialog.askopenfilenames()
print(filename)
print(len(filename))

#this function just checks the filename for the keyword, returns true if it is there, false if not

def search(fname, kword):
    if fname.find(kword) != -1:
        return True
    return False

def returnFilename(fPath):


    return ""

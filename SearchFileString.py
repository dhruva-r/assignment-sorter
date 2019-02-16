from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename = filedialog.askopenfilename()
print(root.filename)
import tkinter
import tkinter.filedialog

filename = tkinter.filedialog.askopenfilenames()
print(filename)
print(len(filename))

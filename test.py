import tkinter
# !/usr/bin/python3
from tkinter import messagebox

top = tkinter.Tk()
top.geometry("200x200")


def hello():
    messagebox.showinfo("Say Hello", "Hello World")


B1 = top.Button(top, text="Say Hello", command=hello)
B1.place(x=35, y=70)

top.mainloop()

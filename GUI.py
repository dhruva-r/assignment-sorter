import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Button for quitting the application
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        # Textbox that contains the entries to be added
        self.entries = tk.Listbox(self)
        self.entries.pack(side = "bottom")

        # Button to add all the entries
        self.add_all = tk.Button(self, text = "Add all")
        self.add_all["command"] = self.complete_dialog
        self.add_all.pack(side = "bottom")

        # Button for adding files to the pending list
        self.add = tk.Button(self, text = "Add", fg = "black")
        self.add["command"] = self.say_hi
        self.add.pack(side = "right")

        # Box and label for accepting files
        self.file_label = tk.Label(self, text = "File: ")
        self.file_label.pack(side= "left")
        self.file_box = tk.Entry(self, bd = 5)
        self.file_box.pack(side = "right")

    def complete_dialog(self):
        messagebox.showinfo("Yay! You're done!", "You have added your selected entries")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

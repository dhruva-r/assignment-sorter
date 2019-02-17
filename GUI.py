import tkinter as tk
from tkinter import messagebox
from tkinter import BOTH, Y

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width = 650, height = 350)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        # Button for quitting the application
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)

        # Textbox that contains the entries to be added
        self.entries = tk.Listbox(self)

        # Scrollbar for the entries
        self.scrollbar = tk.Scrollbar(self)

        # Add the scrollbar into the entry box
        self.entries.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.entries.yview)

        # Button to add all the entries
        self.go = tk.Button(self, text = "GO")
        self.go["command"] = self.complete_dialog

        # Button for adding files to the pending list
        self.add = tk.Button(self, text = "Add", fg = "black")
        self.add["command"] = self.add_entry

        # Box and label for accepting files
        self.file_label = tk.Label(self, text = "Keyword(s): ")
        self.file_box = tk.Entry(self, bd = 5)
        self.directory_path = tk.Entry(self, bd = 5)
        self.confirm = tk.Button(self,text=  "Confirm")

        # Arrange objects
        self.file_label.place(x= 10,y = 15)
        self.file_box.place(x = 60, y =10)
        self.add.place(x = 280, y =15)
        self.directory_path.place(x = 340, y =10)
        self.confirm.place(x = 560, y =15)
        self.entries.place(x = 15, y = 100)
        self.scrollbar.place(x = 200, y = 100, height = 170)
        self.go.place(x = 560, y = 250)

    def complete_dialog(self):
        messagebox.showinfo("Yay! You're done!", "You have added your selected entries")

    def add_entry(self):
        if(self.file_box.get() != ""):
            self.entries.insert(0, self.file_box.get())
            self.file_box.delete(0, 'end')

root = tk.Tk()
app = Application(master=root)
app.mainloop()

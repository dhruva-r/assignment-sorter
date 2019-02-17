import tkinter as tk
from tkinter import messagebox
from tkinter import BOTH, DISABLED, ACTIVE
from Backend import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width = 580, height = 350)
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
        self.go = tk.Button(self, text = "GO", state = DISABLED)
        self.go["command"] = self.assignment

        # Button for adding files to the pending list
        self.add = tk.Button(self, text = "Add", fg = "black")
        self.add["command"] = self.add_entry

        # Button to make changes to the list
        self.delete = tk.Button(self, text = "Delete")
        self.delete["command"] = self.delete_entry

        # Help button
        self.help = tk.Button(self, text = "Help")
        self.help["command"] = self.help_text

        # Box and label for accepting files
        self.keyword_label = tk.Label(self, text = "Keyword(s): ")
        self.keyword_box = tk.Entry(self, bd = 5)
        self.directory_path = tk.Entry(self, bd = 5)
        self.confirm = tk.Button(self,text=  "Confirm")
        self.confirm["command"] = self.new_directory

        # Arrange objects
        self.keyword_label.place(x= 0,y = 10)
        self.keyword_box.place(x = 67, y =10)
        self.add.place(x = 208, y =10)
        self.delete.place(x = 258, y =10)
        self.directory_path.place(x = 344, y =10)
        self.confirm.place(x = 485, y =10)
        self.entries.place(x = 73, y = 100)
        self.scrollbar.place(x = 200, y = 100, height = 170)
        self.go.place(x = 345, y = 100, height = 150, width = 150)
        self.help.place(x = 5, y = 310)

    def delete_entry(self):
        self.entries.delete(ACTIVE)

    def help_text(self):
        messagebox.showinfo("How to use File Sorter", "To get started add some keywords using the top left section"
                                                      ", then use the top right to specify the directory where the "
                                                      "sorted files will be, push confirm then GO. Your files should "
                                                      "be in the new directory in a folder named after the keywords." )

    def new_directory(self):
        if self.directory_path.get() != "":
            set_directory(self.directory_path.get())
            messagebox.showinfo("Setting new Directory",
                            self.directory_path.get() + " is set as the directory you want to move your files")
            self.go['state'] = 'normal'
        else:
            messagebox.showerror("Setting new Directory", "No directory specified")

    def assignment(self):
        for i in range(0,self.entries.size()):
            grab_keywords(self.entries.get(i))
        main()
        messagebox.showinfo("Yay! You're done!", "You have added your selected entries")

    def add_entry(self):
        if(self.keyword_box.get() != ""):
            self.entries.insert(0, self.keyword_box.get())
            self.keyword_box.delete(0, 'end')

root = tk.Tk()
app = Application(master=root)
app.mainloop()

from tkinter import *
from tkinter import ttk
class App():
    def __init__(self):
        self.root = Tk()
        button = ttk.Button(self.root, text = 'root quit', command=self.quit)
        button.pack()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

app = App()

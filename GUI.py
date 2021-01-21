from tkinter import *
from tkinter.ttk import *

class GUI(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)
        master.title("A simple GUI")

        self.canvas = Canvas(master, bd=2, bg="magenta", height = 1000, width = 1000)
        self.canvas.pack()

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def createWidgets(self):
        self.LS = Button(self)
        

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = GUI(root)
root.mainloop()

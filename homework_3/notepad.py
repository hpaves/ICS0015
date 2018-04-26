import tkinter
from tkinter import *
from tkinter import messagebox, scrolledtext, filedialog

# I'm relying on a lot of example code from the lectures by Tauseef Ahmed

# Define main window
root = Tk()
root.geometry("720x400")
root.title("Hnote")

# Create a frame for the text area
textFrame = Frame(root)
textFrame.pack()

# Use ScrolledText widget
scr = scrolledtext.ScrolledText(root, wrap = tkinter.WORD)
scr.pack(side = LEFT, fill = BOTH, expand = YES)

# I want to credit Madis Võrklaev for the idea of putting all the menu functions into a single class
class MenuItems:
    def __init__(self, scr):
        self.scr = scr

    def _new(self):
        self.scr.delete(1.0, END)

    def _open(self):
        root.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        with open(root.filename, "r+") as activefile:
            contents = activefile.read()
            scr.delete(1.0,END)
            scr.insert(tkinter.INSERT, contents)

    def _save(self):
        root.filename = filedialog.asksaveasfilename(title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        with open(root.filename, "w") as activefile:
            contents = scr.get(1.0,END)
            activefile.write(contents)
            activefile.close

    def _quit(self): 
        root.quit()
        root.destroy()
        exit()

    def _about(self):
        messagebox.showinfo("About", "Hnote v0.1\nBy Henri Paves\nThank you, Tauseef Ahmed")

# Create the menu bar and the menuitems object
menuBar = tkinter.Menu(root) 
root.config(menu = menuBar)
hnote = MenuItems(scr)

# Create the menu items and assign them to submenus
fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'New', command = hnote._new)
fileMenu.add_command(label = 'Open', command = hnote._open)
fileMenu.add_command(label = 'Save', command = hnote._save)
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = hnote._quit) 
menuBar.add_cascade(label = 'File', menu = fileMenu)

helpMenu = Menu(menuBar, tearoff = 0)
helpMenu.add_command(label ='About', command = hnote._about)
menuBar.add_cascade(label = 'Help', menu = helpMenu)

# Start the main window (root window)
root.mainloop()

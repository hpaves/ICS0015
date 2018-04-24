import tkinter
from tkinter import *
from tkinter import messagebox, scrolledtext

# I'm relying on a lot of example code from the lectures by Tauseef Ahmed

# Define main window
root = Tk()

# Create a frame for the text area
textFrame = Frame(root)
textFrame.pack()

# Callback function for the Exit menu item
def _quit(): 
    root.quit()
    root.destroy()
    exit()

# Callback function for the About menu item
def aboutWindow():
    tkinter.messagebox.showinfo("About", "Hnote v0.1\nBy Henri Paves\nThank you, Tauseef Ahmed")

# Use ScrolledText
scrollW = 100
scrollH = 40
scr = tkinter.scrolledtext.ScrolledText(root, width = scrollW, height = scrollH, wrap = tkinter.WORD)
scr.pack(side = LEFT, fill = BOTH, expand = YES)

# Fill with content for testing purposes
txt = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ut sapien quis tellus sodales tincidunt at nec enim. Integer tempor odio quis sem condimentum tempus. Donec et lectus neque. Suspendisse gravida, tortor sed dapibus imperdiet, neque mi auctor nulla, id laoreet libero ligula non elit. Duis venenatis in orci sit amet varius. Nullam in urna ex. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nunc pharetra finibus lobortis. Ut rhoncus risus dolor, et tincidunt sapien efficitur id. Donec eu quam justo. Etiam feugiat velit quis consectetur dictum.

Nulla mauris ligula, porttitor quis lorem fringilla, vulputate placerat tortor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi eget diam id tortor ullamcorper sodales. Pellentesque eu semper nulla, vitae imperdiet tortor. Nunc gravida sodales sollicitudin. Suspendisse nisi velit, bibendum ut augue pulvinar, cursus laoreet dui. Phasellus sit amet tincidunt lorem.'''
scr.insert(tkinter.INSERT,txt)

# Create the menu bar
menuBar = tkinter.Menu(root) 
root.config(menu = menuBar)

# Create the menu items and assign them to submenus
fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'New')
fileMenu.add_command(label = 'Open')
fileMenu.add_command(label = 'Save')
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = _quit) 
menuBar.add_cascade(label = 'File', menu = fileMenu)

helpMenu = Menu(menuBar, tearoff = 0)
helpMenu.add_command(label ='About', command = aboutWindow)
menuBar.add_cascade(label = 'Help', menu = helpMenu)

# Start the main window (root window)
root.mainloop()

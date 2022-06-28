import sys
from matplotlib.pyplot import text

from pygame import init
from utils.log_neko import *
import os
from tkinter import *
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
  
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
  
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)
  
# now we can import the module in the parent
# directory.
import adapter
from utils.config_utilities import *

def fill(component, data):
    component.config(state=NORMAL)
    component.insert(data, text)
    component.config(state=DISABLED)

def init_ui():
    """
    COMPONNENTS
    """
    window = Tk()
    text_box = Text(window, width=50, height=10, ).config(state=DISABLED)
    
    btn=Button(window, text="This is Button widget", fg='white')
    btn.place(x=80, y=200)
    """
    COMPONNENTS
    """
    
    """
    PACK
    """
    btn.pack()
    text_box.pack()
    """
    PACK
    """

    """
    BINDING
    """
    btn.bind("<Button-1>", fill(text_box, "Hello World"))
    """
    BINDING
    """

    ## WINDOW
    window.attributes("-topmost", True)
    window.title("MCP")
    window.geometry("500x500")
    window.mainloop()
    ## WINDOW

    
    return window

def use_ui():
    init_ui()
    

if __name__ == '__main__':
    print("THIS IS UI MODULE")
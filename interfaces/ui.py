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
import os # last import (all other imports above this one)
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide' #hide pygame message

window = ""

def fill_textbox(component : Text, data):

    component.config(state=NORMAL)
    component.insert("1.0", data)
    component.config(state=DISABLED)

def clear_textbox(component : Text):

    component.config(state=NORMAL)
    component.delete("1.0", END)
    component.config(state=DISABLED)

def init_ui():
    _window = Tk()
    
    """
    COMPONNENTS
    """
    main_display_text_box = Text(_window, width=50, height=10, )
    main_display_text_box.config(state=DISABLED)
    
    fill_btn=Button(
        _window, 
        text="Fill Button", 
        fg='white', 
        command=lambda: fill_textbox(main_display_text_box, "Hello World")
        )

    clear_btn=Button(
        _window, 
        text="Clear Button", 
        fg='white', 
        command=lambda: clear_textbox(main_display_text_box)
        )
    """
    COMPONNENTS
    """

    """
    BINDING
    """
    #clear_btn.bind("<Button-1>", clear_textbox(text_box))
    #fill_btn.bind("<Button-1>", fill_textbox(text_box, "Hello World"))
    """
    BINDING
    """

    """
    PACK
    """
    main_display_text_box.pack()
    fill_btn.pack()
    clear_btn.pack()
    """
    PACK
    """
    ## WINDOW
    _window.attributes("-topmost", True)
    _window.title("MCP")
    _window.geometry("500x500")
    _window.mainloop()
    ## WINDOW
    

    return _window

# def init_components(_window : Tk):
  


def use_ui():
    window = init_ui()
    return window
    

if __name__ == '__main__':
    print("THIS IS UI MODULE")
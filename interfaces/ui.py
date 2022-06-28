import site
import sys
from turtle import color

from matplotlib.pyplot import text
from pip import main

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

window : Tk

def fill_textbox(component : Text, data):

    component.config(state=NORMAL)
    component.insert("1.0", data)
    component.config(state=DISABLED)

def clear_textbox(component : Text):

    component.config(state=NORMAL)
    component.delete("1.0", END)
    component.config(state=DISABLED)

"""
HELPERS METHODS
"""
def show_credentials(target_component : Text):
    clear_textbox(target_component) # make sure the text box is clear
    data = adapter.list_secured_credentials(retrieve_list=True)
    for _data in data:
        _data = f"[FILE] {_data}\n\n"
        fill_textbox(target_component, _data)
"""
HELPERS METHODS
"""

def init_ui():
    _window = Tk()
    
    """
    COMPONNENTS & BINDING
    """
    main_display_text_box = Text(_window)

    ## NICE ##
    main_display_text_box.config(width=69)
    main_display_text_box.config(border=4)
    main_display_text_box.config(height=20)
    ## NICE ##
    main_display_text_box.config(font=("Courier New", 12))
    main_display_text_box.config()
    main_display_text_box.config(state=DISABLED)

    Label(
        _window, 
        text="My Credential Protector", 
        font=("Poppins, 24")
        ).pack(expand=False, side=TOP)

    # fill_btn=Button(
    #     _window, 
    #     text="Fill Button", 
    #     fg='white', 
    #     command=lambda: fill_textbox(main_display_text_box, "Hello World")
    #     )

    clear_btn=Button(
        _window, 
        text="Clear Main Display", 
        fg='white', 
        command=lambda: clear_textbox(main_display_text_box)
        )
    
    list_cred_btn=Button(
        _window, 
        text="List Your Credentials", 
        fg='white', 
        command=lambda: show_credentials(target_component=main_display_text_box),
        )
    """
    COMPONNENTS & BINDING
    """

    """
    BINDING
    """
    """
    BINDING
    """

    """
    PACK
    """
    main_display_text_box.pack(expand=True, fill=X)
    # fill_btn.pack()
    list_cred_btn.pack(side=LEFT, pady=8, padx=8)
    clear_btn.pack(side=LEFT, pady=8, padx=8)
    """
    PACK
    """
    ## WINDOW
    _window.attributes("-topmost", True)
    _window.title("MCP")
    _window.geometry("500x500")
    _window.configure(pady=10, padx=10)
    _window.mainloop()
    ## WINDOW

    return _window

# def init_components(_window : Tk):
  


def use_ui():
    window = init_ui()
    return window
    

if __name__ == '__main__':
    print("THIS IS UI MODULE")
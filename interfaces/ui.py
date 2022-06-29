from calendar import c
from msilib.schema import ListBox
import sys
from tkinter import messagebox
import os
import ctypes
import pathlib
from tokenize import String
from typing import List

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
# Increas Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)


"""
PROPERTIES
"""
window : Tk
"""
PROPERTIES
"""

"""
HELPERS METHODS
"""

def show_credentials(*event, _list:ListBox):
    # Get all Files and Folders from secured cred dir
    data = adapter.list_secured_credentials(retrieve_list=True)
    # Clearing the list
    _list.delete(0, END)
    # Populating the list
    print("show cred method ui")
    for _data in data:
        _list.insert(0, _data)
        print(_list.get(0))
       

def read_this_credential(_filename:String):
    _filename = _filename.removeprefix("encrypted-")
    data = adapter.read_secured_file(_filename, retrieve_data=True)
    messagebox.showinfo("Decrypted Credential Data", data)


def openTheFile(_list: ListBox, event=None):
    # Get clicked item.
    picked = _list.get(_list.curselection()[0])
    read_this_credential(picked)

def refresh_credentials_list(_list_file:ListBox):
    adapter.rescan_for_new_files()
    show_credentials(_list = _list_file) #refresh the list
"""
HELPERS METHODS
"""

def init_ui():
    _window = Tk()
    
    """
    COMPONNENTS & BINDING
    """
    main_display_box = Frame(_window)
    
    # List of files in secured-credentials directory
    files_list = Listbox(main_display_box)

    ## NICE ##
    files_list.config(width=69)
    files_list.config(border=4)
    files_list.config(height=20)
    ## NICE ##


    Label(
        _window, 
        text="My Credential Protector", 
        font=("Poppins, 24")
        ).pack(expand=False, side=TOP)

    # getting the secured credentials files and populate it ito the list
    show_credentials(_list = files_list)

    scan_for_new_cred_btn=Button(
        _window, 
        text="Scan for new credentials", 
        fg='white', 
        command=lambda: refresh_credentials_list(_list_file = files_list),
        )

    open_btn=Button(
        _window, 
        text="Open", 
        fg='white', 
        command=lambda: openTheFile(files_list, event=None)
        )
    
    
    """
    COMPONNENTS & BINDING
    """

    """
    PACK
    """
    main_display_box.pack( expand=True, fill=BOTH, ipadx=10, ipady=10) #display pack

    files_list.pack( expand=True, fill=X) # list pack

    # buttons pack    
    scan_for_new_cred_btn.pack(side=LEFT, pady=8, padx=8)
    open_btn.pack(side=RIGHT, pady=8, padx=8)
    # buttons pack    


    """
    PACK
    """

    ## WINDOW
    _window.attributes("-topmost", True)
    _window.title("MCP")
    _window.geometry("500x500")
    _window.resizable(False, False)
    _window.configure(pady=10, padx=10)
    _window.mainloop()
    ## WINDOW
 


def use_ui():
    init_ui()
    #window = init_ui()
    #return window
    

if __name__ == '__main__':
    print("THIS IS UI MODULE")
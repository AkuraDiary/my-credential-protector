from calendar import c
from msilib.schema import ListBox
import sys
from tkinter import messagebox
import os
import ctypes
import pathlib
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

# files_list = ListBox()
# currentPath = StringVar()

"""
HELPERS METHODS
"""
def fill_main_frame(component :Frame, btn:Button, _side):
    btn.pack( side=_side, pady=4, padx=4)


def clear_main_frame(component:Frame):
    for widget in component.winfo_children():
        widget.destroy()


# def show_credentials(target_component : Frame):
#     clear_main_frame(target_component) # make sure the text box is clear
    
#     # photo = PhotoImage(file = r".\utils\cred.png").subsample(9)
#     # Clearing the list
#     files_list.delete(0, END)
#     # Inserting the files and directories into the list
#     for file in directory:
#         list.insert(0, file)
#     # for _data in data:

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
       

def read_this_credential(_filename):
    _filename.replace("\n", "")
    _filename.replace("encrypted-", "")
    data = adapter.read_secured_file(_filename, retrieve_data=True)
    messagebox.showinfo("Decrypted Credential Data", data)


def openTheFile(_list: ListBox, event=None):
    # Get clicked item.
    #picked = _files_list.get(_files_list.curselection())
    message_info("open the file")
    message_info(_list.get(_list.curselection()))
    # get the complete path by joining the current path with the picked item
    # path = os.path.picked
    #read_this_credential(picked)

"""
HELPERS METHODS
"""

def init_ui():
    _window = Tk()
    
    """
    COMPONNENTS & BINDING
    """

    main_display_box = Frame(_window)
    
    # List of files and folder
    # files_list = Listbox(main_display_box)
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

    # getting the secured credentials files
    show_credentials(_list = files_list)

    # List Accelerators
    #files_list.bind('<Double-1>', openTheFile(files_list, event=None))

    # fill_btn=Button(
    #     _window, 
    #     text="Fill Button", 
    #     fg='white', 
    #     command=lambda: fill_textbox(main_display_text_box, "Hello World")
    #     )

    open_btn=Button(
        _window, 
        text="Open", 
        fg='white', 
        command=lambda: openTheFile(files_list, event=None)
        )
    
    scan_for_new_cred_btn=Button(
        _window, 
        text="Scan for new credentials", 
        fg='white', 
        # command=lambda: show_credentials(target_component=main_display_box),
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
    main_display_box.pack( expand=True, fill=BOTH, ipadx=10, ipady=10) #display pack

    files_list.pack( expand=True, fill=X) # list pack

    #buttons pack
    open_btn.pack(side=LEFT, pady=8, padx=8)
    scan_for_new_cred_btn.pack(side=LEFT, pady=8, padx=8)
    # clear_btn.pack(side=LEFT, pady=8, padx=8)
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

    #return _window

# def init_components(_window : Tk):
  


def use_ui():
    init_ui()
    #window = init_ui()
    #return window
    

if __name__ == '__main__':
    print("THIS IS UI MODULE")
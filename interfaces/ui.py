import sys
from utils.log_neko import *
import os
import tkinter as tk
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


def init_ui():
    window = tk.Tk()
    window.title("MCP")
    window.geometry("500x500")
    window.mainloop()
    return window

def use_ui():
    init_ui()
    

if __name__ == '__main__':
    print("THIS IS UI MODULE")
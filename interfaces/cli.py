from utils.log_neko import *
import sys
import os
  
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

def use_cli():
    while True:
        print()
        print("MCP CLI MODE")
        print("1. List your Credentials")
        print("2. Read Credentials")
        print("3. Change Token")
        print("4. Change User Account Credentials")
        print("5. Exit")
        print()
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            adapter.list_secured_credentials()

        elif choice == "2":
            filename = input("Enter the filename : encrypted-")
            try:
                adapter.read_secured_file(filename)
            except Exception as e:
                message_warn(e)
                continue
        elif choice == "3":
            adapter.change_token()
        elif choice == "4":
            adapter.change_user_acc_cred()
        elif choice == "5":
            message_info("Exiting MCP CLI Mode")
            exit()
        else:
            message_info("Invalid choice")
            continue

if __name__ == '__main__':
    print("THIS IS CLI MODULE")
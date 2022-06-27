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
        print("Welcome to the CLI")
        print("1. List your Credentials")
        print("2. Read Credentials")
        print("4. Exit")
        print("\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            user_cred_list = adapter.list_secured_credentials()
            print()
            print(user_cred_list)
            print()

        elif choice == "2":
            filename = input("Enter the filename : encrypted-")
            try:
                adapter.read_secured_file(filename)
            except Exception as e:
                message_warn(e)
                continue
        elif choice == "4":
            exit()
        else:
            print("Invalid choice")
            continue

if __name__ == '__main__':
    print("THIS IS CLI MODULE")
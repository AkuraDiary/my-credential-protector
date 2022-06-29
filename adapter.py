from core import *
from interfaces.cli import *
from interfaces.ui import *

config = load_config("config.json")
"""
ADAPTER METHODS
"""
def read_secured_file(filename, retrieve_data=False):
    filename = "encrypted-" + filename
    print()
    decrypted_data = read_encrypted_file(filename)
    if retrieve_data:
        return decrypted_data
    else:
        message_info("Decrypted data")
        print(decrypted_data)
        print()
        message_info("Decrypted data")

def list_secured_credentials(retrieve_list=False):
    _lists = list_files_in_dir(config["cred-output-dir"])
    _lists.remove(".gitignore")
    if retrieve_list:
        return _lists
    else:
        print("List of secured credentials : \n")
        for file in _lists:
            print("[ FILE ] : " + file)
        

def change_token():
    message_warn("Warning, this is will change your token and you might won't be able to use it to read your previeous encrypted file")
    choice = input("Are you sure you want to continue? (y/n): ")
    print()
    if choice == "y":
        
        init_token()
        load_user_token()
        message_info("You Have to restart the programs in order to apply the changes")
        
    else:
        message_info("Token not changed")

def change_user_acc_cred():
    message_warn("Warning, this is will change your user account and master password")
    choice = input("Are you sure you want to continue? (y/n): ")
    print()
    if choice == "y":
        cli_do_auth()
        init_user_auth()
    else:
        message_info("User account not changed")

def rescan_for_new_files():
    scan_credentials_dir()

def check_for_updates():
    message_info("Checking for updates")
    update()

"""
ADAPTER METHODS
"""

def main():
    start()
    mode = input("Enter mode (cli / ui): ")
    print()
    mode.strip()
    if mode == "cli":
        try:
            use_cli()
        except KeyboardInterrupt:
            message_info("Exiting MCP CLI Mode")
            exit()
    elif mode == "ui":
        message_info("Initializing MCP UI Mode")
        message_warn("DO NOT CLOSE THIS TERMINAL")
        use_ui()
    else:
        message_warn("Invalid mode")
        message_info("Using Default CLI")
        use_cli()

if __name__ == "__main__":
    print("THIS IS ADAPTER MODULE")
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
    message_warn("Warning, this is will change your token and \nYOU WON'T BE ABLE TO USE THE TOKEN TO READ YOU PREVIOUSLY ENCRPYTED CREDENTIALS")
    choice = input("Are you sure you want to continue? (y/n): ")
    print()
    if choice == "y":
        auth_response = cli_do_auth(sendResponse=True) #get the previous credentials, because credential hashing is binded with token
        username, password, response = auth_response[0], auth_response[1], auth_response[2]
        if(response):
            init_token()
            load_user_token()
            ### update the user cred hash
            user_cred_config = config["usr-cred-file"]
            hashedUsrname = hash_string(username + user_token)
            hashedPassword = hash_string(password + user_token)
            add_entry_to_config(user_cred_config, "username", hashedUsrname)
            add_entry_to_config(user_cred_config, "password", hashedPassword)
            ### update the user cred hash
            
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
    do_backup()
    message_info("Checking for updates")
    update()
    


def add_credentials(_filename:String):
    if ".txt" not in _filename:
        _filename += ".txt"
    target_dir = config["cred-input-dir"]
    target_file = target_dir + "\\"+ _filename
    
    open(target_file, "w").close()
    os.startfile(target_file)

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
        message_info("Using Default UI MODE")
        try:
            use_ui()
        except Exception as e:
            message_warn(e)
            message_info("Switching into CLI Mode")
            use_cli()

if __name__ == "__main__":
    print("THIS IS ADAPTER MODULE")
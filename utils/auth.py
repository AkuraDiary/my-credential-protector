"""
AUTH METHODS
"""
from utils.config_utilities import *
from utils.log_neko import *
from utils.validation import *
from getpass import getpass

config = load_config("config.json")
tokenFile = load_config(config["cipher-token-file"])
user_token = tokenFile["token"] #get user token

def update_auth_hash(_username, _password):
    message_info("Trying updating auth hash")

    user_cred_config = config["usr-cred-file"]


    newHashedUsrname = hash_string(_username + user_token)
    newHashedPass = hash_string(_password + user_token)

    add_entry_to_config(user_cred_config, "username", newHashedUsrname)
    add_entry_to_config(user_cred_config, "password", newHashedPass)
    
    
    message_info("Auth hash updated")
    

def do_login(_username, _password):
    message_info("Logging in")

    user_cred_config = config["usr-cred-file"]
    
    password = _password + user_token
    username = _username + user_token

    usernameIsValid = validate_string_hash(username, load_config(user_cred_config)["username"] )
    passIsValid = validate_string_hash(password, load_config(user_cred_config)["password"])
        

    if usernameIsValid and passIsValid:
        message_info("Login success")
        return True
    else:
        message_warn("Login failed")
        update_auth_hash(_username, _password)    
        message_info("Please Re run the program")
        exit()
       
            

    # if usernameIsValid:
    #     message_warn("Username is invalid")
    #     try:
    #         update_auth_hash(username, password)
    #         message_info("Re run the programs")
    #     except Exception as e:
    #         raise Exception("Failed to update auth hash", e)
    # else:
    #     if load_config(user_cred_config)["password"] == hashedPassword:
    #         message_info("Login success")
    #         return True
    #     else:
    #         message_warn("Login failed")
    #         raise Exception("Invalid password")

def cli_do_auth():
    message_info("Authenticating")
    username = input("Enter your username: ")
    password = getpass("Enter your master password: ")
    print()
    try:
        return do_login(username, password)
    except Exception as e:
        message_warn(e)
        return False
        
"""
AUTH METHODS
"""


if __name__ == '__main__':
    print("THIS IS AUTH MODULES TODO (ADD DOCUMENTATION)")
    do_login()

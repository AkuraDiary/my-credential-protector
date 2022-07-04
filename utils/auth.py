"""
AUTH METHODS
"""
from utils.config_utilities import *
from utils.log_neko import *
from utils.validation import *
from getpass import getpass
import sys

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
        oldHash = {
            "usrname" : validate_string_hash(_username, load_config(user_cred_config)["username"]), 
            "pass": validate_string_hash(_password, load_config(user_cred_config)["password"])
            }
        if(oldHash["usrname"] and oldHash["pass"]):
            message_info("Trying to check the oldhash")
            message_info("Old hash is valid")
            update_auth_hash(_username, _password)
            message_info("Please Re run the program")
            return True
        sys.exit()
  

def cli_do_auth(sendResponse=False):
    message_info("Authenticating")
    username = input("Enter your username: ")
    password = getpass("Enter your master password: ")
    print()
    try:
        if sendResponse:
            return username, password, do_login(username, password)
        else:
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

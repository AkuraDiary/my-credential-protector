"""
AUTH METHODS
"""
from utils.config_utilities import *
from utils.log_neko import *
from utils.validation import *
from getpass import getpass

config = load_config("config.json")
def do_login(username, password):
    message_info("Logging in")
    user_cred_config = config["usr-cred-file"]
    
    hashedPassword = hash_string(password)
    hashedUsername = hash_string(username)
    if load_config(user_cred_config)["username"] != hashedUsername:
        raise Exception("Invalid Username")
    else:
        if load_config(user_cred_config)["password"] == hashedPassword:
            message_info("Login success")
            return True
        else:
            message_warn("Login failed")
            raise Exception("Invalid password")

def do_auth():
    message_info("Authenticating")
    username = input("Enter your username: ")
    password = getpass("Enter your master password: ")
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

"""
AUTH METHODS
"""
from utils.config_utilities import *
from utils.log_neko import *
from utils.validation import *

config = load_config("config.json")
def do_login(username, password):
    message_info("Logging in")
    user_cred_config = config["usr-cred-file"]
    
    hashedPassword = hash_string(password)
    hashedUsername = hash_string(username)
    if load_config(user_cred_config)["username"] == hashedUsername:
        message_info("Username is correct")
        if load_config(user_cred_config)["password"] == hashedPassword:
            message_info("Login success")
            return True
        return False
    else:
        message_warn("Login failed")
        return False

"""
AUTH METHODS
"""


if __name__ == '__main__':
    print("THIS IS AUTH MODULES TODO (ADD DOCUMENTATION)")
    do_login()

from asyncio import subprocess
from multiprocessing.connection import wait

from gevent import config
from rsa import PrivateKey
from utils.validation import *
from utils.config_utilities import *
import subprocess
from utils.log_neko import *

"""
INIT TOOLS METHODS
"""
config = load_config("config.json")
def isFirstRun():
    return config["isFirstRun"]

def init_first_run_sequence():
    message_info("Initializing first run sequence")
    
    message_info("Loading config file")
    
    satisfy_dependencies()

    message_info("Initializing empty user-config files")
    init_config(filenames = config)
    
    message_info("changed first run status to false")
    add_entry_to_config("config.json","isFirstRun", False)

    message_info("succesfully runned first run sequence")

def init_config(filenames):
    open(filenames["cipher-token-file"], "w").close()
    open(filenames["usr-cred-file"], "w").close()
    open(filenames["hashes-file"], "w").close()

def init_user_auth():
    message_info("Initializing User Authentication")
    user_cred_config = config["usr-cred-file"]
    username = input("Enter your username: ")
    password = input("Enter your master password: ")

    hashedUsrname = hash_string(username)
    hashedPassword = hash_string(password)

    add_entry_to_config(user_cred_config, "username", hashedUsrname)
    add_entry_to_config(user_cred_config, "password", hashedPassword)
    message_info("succesfully added user credentials")

    
def init_token(): 
    message_info("Initializing Token Generation")
    token = ""
    privateKey = ""
    
    message_info("generating user token")
    
    from sigma_ciphers_cryptograms import core
    sigma = core.Sigma()
    tokenLen = int(input("Enter your token length: "))
    token = sigma.generate_token(tokenLen)
    privateKey = sigma.generate_private_key(token)

    add_entry_to_config(config["cipher-token-file"], "token", token)
    add_entry_to_config(config["cipher-token-file"], "private-key", hash_string(privateKey))
    

def init_on_start():
    message_info("Initializing")
    message_info("Scanning for a new file in .\\credentials")
    newFileList = scan_for_new_file(config["cred-input-dir"])

    if newFileList is not None:
        message_info(newFileList)

        message_info("TODO Encrypting new file")
        #TODO ENCRYPT THE FILE
        message_info("TODO Succesfully encrypted new file")

        message_info("Moving new file to .\\secured-credentials")
        for file in newFileList:
            makeCopyOfFile(file, "new content" ,path = config["cred-output-dir"])
        message_info("succesfully moved new files to .\\secured-credentials")
        clear_dir(load_config("config.json")["cred-input-dir"])

"""
INIT TOOLS METHODS
"""


"""
FILE TOOLS METHOD
"""
def scan_for_new_file(dir_path):
    file_list = list_supported_files_in_dir(dir_path)
    if len(file_list) > 1:
        message_info("Found new file in dir")
        file_list.remove(".gitignore")
        return file_list
    else:
 
        message_info("No new file found in dir")
        return None

def clear_dir(dir_path):
    message_info("clearing directory", dir_path)
    file_list = list_files_in_dir(dir_path)
    if(len(file_list) <= 1):
        message_info("directory is empty")
        return
    for file in file_list:
        if(".txt" in file):
            try:
                os.remove(dir_path + "\\" + file)
                message_info("succesfully removed" , file)
            except Exception as e:
                message_warn(e)
                print()
    message_info("succesfully cleared" , dir_path)


"""
FILE TOOLS METHOD
"""


"""
DEPENDENCIES TOOLS
"""
repos_link = load_config("repositories.json")

def clone(repos):
    try:
        subprocess.Popen(['git', 'clone' , "--branch", "modular",  repos], shell=True)
        message_info("succesfully cloned" , repos)
    except Exception as e:
        message_warn(e)
        print()#space

def pull(path):
    try:
        subprocess.Popen(['git', 'pull'], cwd=path, shell=True)
        message_info("succesfully updated" , path)
    except Exception as e:
        print(e)
    
def satisfy_dependencies():
    message_info("Cloning all required dependencies repos")
    for repos in repos_link:
        clone(repos_link.get(repos))
    message_info("succesfully cloned all required dependencies repos")

def update():
    try:
        pull(load_config("config.json")["cipher_path"])
        pull(load_config("config.json")["mcp_path"])
        message_info("succesfully doing update")
    except Exception as e:
        message_warn(e)
        print()#space
"""
DEPENDENCIES TOOLS
"""
if __name__ == '__main__':
    print("THIS IS TOOLS MODULES TODO (ADD DOCUMENTATION)")

    ### TESTING
    init_token()
    #init_user_auth()
    #init_on_start() DONE
    #clear_dir(load_config("config.json")["cred-input-dir"]) DONE
    #init_first_run_sequence() DONE

from asyncio import subprocess
import asyncio
from sigma_ciphers_cryptograms.core import Sigma
from utils.validation import *
from utils.config_utilities import *
import subprocess
from utils.log_neko import *


config = load_config("config.json")


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

async def clone(repos):
    try:
        subprocess.Popen(['git', 'clone' , "--branch", "modular",  repos], shell=True)
        message_info("succesfully cloned" , repos)
    except Exception as e:
        message_warn(e)
        print()#space

async def pull(path):
    try:
        message_info("Updating", path)
        subprocess.Popen(['git', 'pull'], cwd=path, shell=True)
    except Exception as e:
        print(e)
    
def satisfy_dependencies():
    message_info("Cloning all required dependencies repos")
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(clone(repos_link["cipher"]))
    
    message_info("succesfully cloned all required dependencies repos")

def update():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(pull(load_config("config.json")["cipher_path"]))
        loop.run_until_complete(pull(load_config("config.json")["mcp_path"]))
    except Exception as e:
        message_warn(e)
        print()#space
    finally:
        message_info("Please re-run the program to apply changes")
"""
DEPENDENCIES TOOLS
"""

"""
BACKUP CONVINENCE METHODS TOOLS
"""

"""
BACKUP CONVINENCE METHODS TOOLS
"""

if __name__ == '__main__':
    print("THIS IS TOOLS MODULES TODO (ADD DOCUMENTATION)")

    ### TESTING
    #init_token()
    #init_user_auth()
    #init_on_start() DONE
    #clear_dir(load_config("config.json")["cred-input-dir"]) DONE
    #init_first_run_sequence() DONE

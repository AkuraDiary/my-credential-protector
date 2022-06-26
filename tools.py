from asyncio import subprocess
from multiprocessing.connection import wait

from gevent import config
from utils.config_utilities import *
import subprocess
from utils.log_neko import *

"""
INIT TOOLS METHODS
"""
def init_first_run_sequence():
    message_info("Initializing first run sequence")
    
    message_info("Loading config file")
    config = load_config("config.json")
    
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
"""
INIT TOOLS METHODS
"""

"""
FILE TOOLS METHOD
"""
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
                #subprocess.Popen(['rm', file], cwd=dir_path, shell=True)
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
        subprocess.Popen(['git', 'clone' , repos], shell=True)
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
    print("THIS IS TOOLS MODULES TODO ADD DOCUMENTATION")
    clear_dir(load_config("config.json")["cred-input-dir"])
    #init_first_run_sequence()
    #satisfy_dependencies()
    #repos = "https://github.com/AkuraDiary/sigma-ciphers-cryptograms.git"
    
    #clone(repos)
    #pull("./sigma-ciphers-cryptograms")
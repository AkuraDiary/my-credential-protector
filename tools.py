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
DEPENDENCIES TOOLS
"""
repos_link = load_config("repositories.json")

def clone(repos):
    try:
        subprocess.Popen(['git', 'clone' , repos], shell=True)
        message_info("succesfully cloned" , repos)
    except Exception as e:
        print(e)

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
        message_info("succesfully updated")
    except Exception as e:
        print(e)
"""
DEPENDENCIES TOOLS
"""
if __name__ == '__main__':
    print("THIS IS TOOLS MODULES TODO ADD DOCUMENTATION")
    init_first_run_sequence()
    #satisfy_dependencies()
    #repos = "https://github.com/AkuraDiary/sigma-ciphers-cryptograms.git"
    
    #clone(repos)
    #pull("./sigma-ciphers-cryptograms")
from asyncio import subprocess
from utils.config_utilities import *
import subprocess


"""
DEPENDENCIES TOOLS
"""
repos_link = load_config("repositories.json")

def clone(repos):
    try:
        subprocess.Popen(['git', 'clone' , repos], shell=True)
        print("succesfully cloned" , repos)
    except Exception as e:
        print(e)

def pull(path):
    try:
        subprocess.Popen(['git', 'pull'], cwd=path, shell=True)
        print("succesfully updated" , path)
    except Exception as e:
        print(e)
    
def satisfy_dependencies():
    for repos in repos_link:
        clone(repos_link.get(repos))
    print("succesfully cloned all required dependencies repos")

def update():
    try:
        pull(load_config("config.json")["cipher_path"])
        pull(load_config("config.json")["mcp_path"])
        print("succesfully updated")
    except Exception as e:
        print(e)
"""
DEPENDENCIES TOOLS
"""
if __name__ == '__main__':
    print("THIS IS TOOLS MODULES TODO ADD DOCUMENTATION")
    #satisfy_dependencies()
    #repos = "https://github.com/AkuraDiary/sigma-ciphers-cryptograms.git"
    
    #clone(repos)
    #pull("./sigma-ciphers-cryptograms")
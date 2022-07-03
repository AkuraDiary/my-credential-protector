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
BACKUP CONVINENCE METHODS TOOLS
"""
def do_backup():
    #check if backup folder exists
    backup_path = config["backup-path"]
    secured_cred_path = config["cred-output-dir"]
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
    #copy all and decrypt files in secured credentials to backup folder
    message_info("Backing up files")
    encrypted_file_list = list_files_in_dir(secured_cred_path)
    if encrypted_file_list is not None:
        import core
        encrypted_file_list.remove(".gitignore")
        message_info("Creating Backup")
        
        #Decrypt the files and move it into backup
        for file in encrypted_file_list:
            try:
                data = core.read_encrypted_file(file)
                #strip "encrypted-" from filename
                filename = file.replace("encrypted-", "")
                makeCopyOfFile(oldFileName = filename, newContent= data, status="backup", path=backup_path)
            except Exception as e:
                message_warn(e)
                print()
        
        message_info("Succesfully doing backup")
     
        # clear_dir(backup_path)
def import_backup():
    message_info("Importing backup files")
    backup_path = config["backup-path"]
    
    backupFileList = list_files_in_dir(backup_path)
    cred_path = config["cred-input-dir"]
    if backupFileList is not None:
        message_info(backupFileList)
        for file in backupFileList:
            try:
                file_path = backup_path + "\\" + file
                data = readFileContent(file_path)

                #remove the state from original filename
                filename = file.replace("backup-", "")
                # move file into cred-input-dir
                with open(cred_path + "\\" + filename, "w") as f:
                    f.write(data)                
            except Exception as e:
                message_warn(e)     
        message_info("Succesfully imported backup files")
        #remove backup dir
        message_info("Removing backup directory")
        os.popen("rd /s /q " + backup_path)  
"""
BACKUP CONVINENCE METHODS TOOLS
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

if __name__ == '__main__':
    print("THIS IS TOOLS MODULES TODO (ADD DOCUMENTATION)")

    ### TESTING
    #init_token()
    #init_user_auth()
    #init_on_start() DONE
    #clear_dir(load_config("config.json")["cred-input-dir"]) DONE
    #init_first_run_sequence() DONE

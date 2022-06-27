# Import goes brrr
from time import sleep
import sigma_ciphers_cryptograms
from utils.auth import *
from utils.log_neko import message_info
from utils.file_utilities import *
from utils.config_utilities import *
from tools import *
from utils.validation import *
import threading

user_token = ""
user_private_key = ""
config = load_config("config.json")

"""
INIT HELPER METHODS
"""
def loadSigma():
    from sigma_ciphers_cryptograms import core as sigma_core
        
    _sigma = sigma_core.Sigma()
    message_info("Succesfully loaded sigma")
    return _sigma
        

def loading_token():
    
    message_info("Loading token...")

    tokenFile = load_config(config["cipher-token-file"])
    
    user_token = tokenFile["token"]

    message_info("Loading private key...")
    user_private_key_hash = tokenFile["private-key"]
    message_info("Validating private key")
    user_private_key = validate_private_key(user_token, user_private_key_hash)
    if user_private_key:
         message_info("Succesfully loaded token and private key")
    else:
        message_warn("Failed to load token and private key")
        message_warn("Please restart the application")
        exit()
           
def validate_private_key(token, privateKeyHash):
    sigma=loadSigma()
    privateKey = sigma.generate_private_key(token)
    if validate_string_hash(privateKey, privateKeyHash):
        message_info("Private key is valid")
        return privateKey
    else:
        message_warn("Private key is invalid")
        return False
"""
INIT HELPER METHODS
"""

"""
INIT METHODS
"""
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
    
    if(cli_do_auth()):
        message_info("Scanning for a new file in .\\credentials")
        newFileList = scan_for_new_file(config["cred-input-dir"])
        
        if newFileList is not None:
            message_info(newFileList)
            message_info("Encrypting new file")
            
            #Encrypt new file
            for file in newFileList:
                try:
                    encrypt_file(file)
                except Exception as e:
                    message_warn(e)
                    print()
            
            message_info("Succesfully encrypted new file")
         
            clear_dir(load_config("config.json")["cred-input-dir"])
    else:
        message_warn("User Authentication failed")
        message_warn("Exiting")
        exit()

def init_core_module():
    
    message_info("Initializing core")
    if isFirstRun():
        init_first_run_sequence()
        
        sleep(3.5)

        init_user_auth()
        init_token()

    
    message_info("Initialization completed")

"""
INIT METHODS
""" 

"""
METHOD THAT CONNECTS INTO SIGMA MODULE
"""
def encrypt_file(filename):
    sigma = loadSigma()
    message_info("Encrypting file : " , filename)
    print(user_token)
    data = ""
    encrypted_data = ""
    secured_path = config["cred-output-dir"]
    file_path = config["cred-input-dir"] + "\\" + filename

    data = readFileContent(file_path)
    encrypted_data = sigma.start_encode(data, user_token)
    
    message_info("Moving new file to .\\secured-credentials")
    encrypted_filename = makeCopyOfFile(filename, encrypted_data, path=secured_path, retrieve_fileName=True)
    message_info("succesfully moved new files to .\\secured-credentials") 

    message_info("generating hash for file")
    
    file_hash = hash_file(encrypted_filename)
    if(file_hash is  None):
        raise Exception("Failed to generate hash for file")

    message_info("store file's hash")
    hash_config = config["hashes-file"]

    add_entry_to_config(hash_config, encrypted_filename, file_hash)
    message_info("succesfully encrypted file and stored file's hash")

def read_encrypted_file(filename):
    sigma = loadSigma()
    message_info("Reading file : " , filename)

    data = ""
    decrypted_data = ""
    secured_path = config["cred-output-dir"]
    file_path = secured_path + "\\" + filename

    message_info("Retrieving file's hash")
    hash_config = config["hashes-file"]
    file_hash = load_config(hash_config)[file_path]

    message_info("Validating file's hash")
    if (validate_file_hash(file_path, file_hash)):
        message_info("File's hash is valid")
        data = readFileContent(file_path)
        decrypted_data = sigma.start_decode(data, user_private_key)
        
        print()
        message_info("Decrypted data : ")
        print(decrypted_data)
        message_info("Decrypted data")
        print()

    else:
        message_warn("File's hash is invalid")
    
"""
METHOD THAT CONNECTS INTO SIGMA MODULE
"""

def start():
    """
    Wrapper method for starting the program
    """
    init_core_module()
    loading_token()
    init_on_start()

if __name__ == '__main__':
    print("THIS IS CORE MODULE")
    start()
    #init_user_auth()
    #username = str(input("Enter your username: "))
    #password = str(input("Enter your master password: "))
    #do_login(username, password)

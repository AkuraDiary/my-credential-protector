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

def loadSigma():
    from sigma_ciphers_cryptograms import core as sigma_core
        #sigma_core.Sigma()
    _sigma = sigma_core.Sigma()
    message_info("Succesfully loaded sigma")
    return _sigma
        
    
#sigma = threading.Thread(target=loadSigma)

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
    if hash_string(privateKey) == privateKeyHash:
        message_info("Private key is valid")
        return privateKey
    else:
        message_warn("Private key is invalid")
        return False
    
def init_adapter():
    
    message_info("Initializing adapter")
    if isFirstRun():
        init_first_run_sequence()
        
        sleep(3.5)

        init_user_auth()
        init_token()

    
    message_info("Initialization completed")
    

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
        

if __name__ == '__main__':
    print("THIS IS ADAPTER MODULE TO CONECTING THE PROCESS BETWEEN CORE AND MAIN")
    init_adapter()
    loading_token()
    init_on_start()
    read_encrypted_file("encrypted-dummy-file.txt")
    #init_user_auth()
    #username = str(input("Enter your username: "))
    #password = str(input("Enter your master password: "))
    #do_login(username, password)

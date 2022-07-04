from hashlib import sha256

from utils.config_utilities import *
from utils.file_utilities import *

HASH_CONFIG_FILENAME = load_config("config.json")["hashes-file"]
tempDict = {}


"""
CORE METHODS IN THIS MODULE
"""
def hash_string(string):
    return sha256(string.encode()).hexdigest()

def validate_string_hash(data, hash):#FOR STRING
    #check if the hash is correct
    if hash_string(data) == hash:
        return True
    else:
        return False

def validate_file_hash(filename, hash):#FOR FILE
    #check if the hash is correct
    if hash_file(filename) == hash:
        return True
    else:
        return False

def hash_file(filename):
    #hash the file content
    content = readFileContent(filename)
    if content is not None:
        return hash_string(content)
    else:
        return None
"""
CORE METHODS IN THIS MODULE
"""

"""
CONVINIENT MENTHODS
"""
def generate_newFileHash(_file):
    add_entry_to_config(HASH_CONFIG_FILENAME, _file, hash_file(_file))

def generate_newStringHash(name, data):
    add_entry_to_config(HASH_CONFIG_FILENAME, name, hash_string(data))

def saveTempData(name: str, value: str):
    tempDict[name] = value
"""
CONVINIENT MENTHODS
"""

if __name__ == '__main__':
    print("file validation practice\n")
    
    print("HASHING AND VALIDATING STRING \n")
    a_string = 'this string holds important and private information'
    hashed_string = hash_string(a_string)
    

    saveTempData("a_string", hashed_string)

    add_entry_to_config(HASH_CONFIG_FILENAME,"a_string", hashed_string)

    print("VALIDATION")

    _hash = load_config()["a_string"]
    
    if(validate_string_hash(a_string, _hash)):
        print(f"HASH for {a_string} IS VALID")
    else:
        print(f"HASH for {a_string} IS INVALID")
    
    print("HASHING AND VALIDATING STRING \n")

    print("HASHING AND VALIDATING A FILE \n")
    
    filename = "dummy-file.txt"
    
    hashed_file = hash_file(filename)
    
    print(f"Data : {filename}")
    
    saveTempData(filename, hashed_file)
    add_entry_to_config(HASH_CONFIG_FILENAME,filename, hashed_file)

    print("VALIDATION")
    
    _hash = load_config()[filename]
    
    if(validate_file_hash(filename, _hash)):
        print(f"HASH for {filename} IS VALID")
    else:
        print(f"HASH for {filename} IS INVALID")

    print("HASHING AND VALIDATING A FILE \n")
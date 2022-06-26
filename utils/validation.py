
# Hash a single string with hashlib.sha256
from hashlib import sha256
import json
import os

from tomlkit import string

HASH_CONFIG_FILENAME = "hashes.json"
ENCODING = "utf-8"
tempDict = {}


"""
FILE IO METHODS
"""
def fileIsExist(filename):
    return os.path.exists(filename)

def readFileContent(filename):
    #read the file content, no matter it's from a path or dir / path
    if fileIsExist(filename):
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                return f.read()
        except:
            raise Exception("cannot read file contents")
    else:
        return None

def is_empty(filename) -> bool:
    """
        Check if a file is empty
    """
    return os.path.getsize(filename) == 0

"""
FILE IO METHODS
"""

"""
CORE METHODS IN THIS MODULE
"""

def hash_string(string):
    return sha256(string.encode()).hexdigest()

def validate_string_hash(data: string, hash: string):#FOR STRING
    #check if the hash is correct
    if hash_string(data) == hash:
        return True
    else:
        return False

def validate_file_hash(filename: string, hash: string):#FOR FILE
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
    add_entry_to_config(_file, hash_file(_file))

def generate_newStringHash(name, data):
    add_entry_to_config(name, hash_string(data))
"""
CONVINIENT MENTHODS
"""


"""
CONFIG IO UTILS METHODS
"""
def load_config() -> dict:
    """
        Load config into a dictionary
    """
    if not os.path.exists(HASH_CONFIG_FILENAME) or is_empty(HASH_CONFIG_FILENAME):
        return {}

    with open(HASH_CONFIG_FILENAME, "r", encoding=ENCODING) as config:
        return json.load(config)

def save_to_config(config) -> None:
    """
        Save a dict to config file
    """

    with open(HASH_CONFIG_FILENAME, "w", encoding=ENCODING) as config_file:
        json.dump(config, config_file)

def add_entry_to_config(name: str, value: str):
    config = load_config()

    config[name] = value

    save_to_config(config)

def saveTempData(name: str, value: str):
    tempDict[name] = value
"""
CONFIG IO UTILS METHODS
"""

if __name__ == '__main__':
    print("file validation practice\n")
    
    print("HASHING AND VALIDATING STRING \n")
    a_string = 'this string holds important and private information'
    hashed_string = hash_string(a_string)
    

    saveTempData("a_string", hashed_string)

    add_entry_to_config("a_string", hashed_string)

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
    add_entry_to_config(filename, hashed_file)

    print("VALIDATION")
    
    _hash = load_config()[filename]
    
    if(validate_file_hash(filename, _hash)):
        print(f"HASH for {filename} IS VALID")
    else:
        print(f"HASH for {filename} IS INVALID")

    print("HASHING AND VALIDATING A FILE \n")
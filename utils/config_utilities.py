import json
import os
from utils.file_utilities import *

ENCODING = "utf-8"
"""
CONFIG IO UTILS METHODS
"""

def load_config(filename) -> dict:
    """
        Load config into a dictionary
    """
    if not os.path.exists(filename) or is_empty(filename):
        return {}

    with open(filename, "r", encoding=ENCODING) as config:
        return json.load(config)

def save_to_config(filename, config) -> None:
    """
        Save a dict to config file
    """
    with open(filename, "w", encoding=ENCODING) as config_file:
        json.dump(config, config_file)

def add_entry_to_config(filename, name: str, value: str):
    config = load_config(filename)

    config[name] = value

    save_to_config(filename, config)

"""
CONFIG IO UTILS METHODS

"""

if __name__ == '__main__':
    print("THIS IS CONFIG UTILITIES MODULE")
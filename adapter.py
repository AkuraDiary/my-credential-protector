from core import *
from interfaces.cli import *

config = load_config("config.json")
"""
ADAPTER METHODS
"""
def read_secured_file(filename):
    filename = "encrypted-" + filename
    print()
    decrypted_data = read_encrypted_file(filename)
    message_info("Decrypted data")
    print(decrypted_data)
    print()
    message_info("Decrypted data")

def list_secured_credentials():
    _lists = list_files_in_dir(config["cred-output-dir"])
    _lists.remove(".gitignore")
    print("List of secured credentials : \n")
    for file in _lists:
        print("[ FILE ] : " + file)

"""
ADAPTER METHODS
"""

def main():
    start()
    mode = input("Enter mode (cli / ui): ")
    mode.strip()
    if mode == "cli":
        use_cli()
    elif mode == "ui":
        message_info("UI mode not implemented yet")
        #use_ui()
    else:
        message_warn("Invalid mode")
        message_info("Using Default CLI")
        use_cli()

if __name__ == "__main__":
    print("THIS IS ADAPTER MODULE")
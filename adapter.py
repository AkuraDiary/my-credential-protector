
from json import tool
from sqlite3 import adapt
from utils.log_neko import message_info

# Import goes brrr
from utils.file_utilities import *
from utils.config_utilities import *
from tools import *
from utils.validation import *


if __name__ == '__main__':
    print("THIS IS ADAPTER MODULE TO CONECTING THE PROCESS BETWEEN CORE AND MAIN")
    message_info("I think i should tests my methods here")
    init_first_run_sequence()
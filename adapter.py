# Import goes brrr
from utils.log_neko import message_info
from utils.file_utilities import *
from utils.config_utilities import *
from tools import *
from utils.validation import *
import threading

def init_adapter():
    if isFirstRun():
        t = threading.Thread(target = init_first_run_sequence())
        t.start()
    t.join()
    init_on_start()
    try:
        from sigma_ciphers_cryptograms import core
    except ModuleNotFoundError:
        message_warn("Sigma Ciphers Cryptograms is not installed")
        message_warn("Please wait, until it is installed")
        

        

if __name__ == '__main__':
    print("THIS IS ADAPTER MODULE TO CONECTING THE PROCESS BETWEEN CORE AND MAIN")
    init_adapter()

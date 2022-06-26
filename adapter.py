# Import goes brrr
from time import sleep
from utils.log_neko import message_info
from utils.file_utilities import *
from utils.config_utilities import *
from tools import *
from utils.validation import *
import threading

global sigma 
def init_adapter():
    message_info("Initializing adapter")
    if isFirstRun():
        init_first_run_sequence()
        
        sleep(3.5)

        init_user_auth()
        init_token()
    
    init_on_start()
    
    try:
        from sigma_ciphers_cryptograms import core as sigma_core
        global sigma #sigma_core.Sigma()
        sigma = sigma_core.Sigma()
    except ModuleNotFoundError:
        message_warn("Sigma Ciphers Cryptograms is not installed")
        message_warn("Please wait, until it is installed")
  
    message_info("Initialization completed")

    
        

        

if __name__ == '__main__':
    print("THIS IS ADAPTER MODULE TO CONECTING THE PROCESS BETWEEN CORE AND MAIN")
    init_adapter()

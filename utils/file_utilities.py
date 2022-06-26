import os
import ntpath

from utils.log_neko import *

"""
FILE IO METHODS
"""
def is_empty(filename) -> bool:
    """
        Check if a file is empty
    """
    return os.path.getsize(filename) == 0

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

def path_leaf(path):
    #get the file name from the path
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def fileSupported(filename):
    # check if the file is supported or not
    if fileIsExist(filename):
        try:
            with open(filename, 'r', encoding="utf_8") as f:
                f.read()
            return True
        except Exception as E:
            print(E)
            return False

def list_supported_files_in_dir(dir_path):
    #list all "only" files in a directory
    _Lists = os.listdir(dir_path)
    message_info("Scanning supported file in dir....")
    for file in _Lists: #file recognition / testing the it's the file or not (anjay file recognition)
        try:
            if fileSupported(dir_path + file):
                message_info("file : " + file , "is supported\n")
        except Exception as e:
            message_warn("Warning: {} {}".format( file, e))
            _Lists.remove(file)
            message_warn("Removed from list : " , file)
    #print("list of supported files : ", _Lists)
    return _Lists

def list_files_in_dir(dir_path):
    #list all "only" files in a directory with no scanning
    _Lists = os.listdir(dir_path)
    message_info("Scanning files in dir....")
    return _Lists

def makeCopyOfFile( oldFileName, newContent, path="", status = "encrypted", retrieve_fileName = False):
    if path != "":
        path = path + "\\"
    newFileName = path + status + "-"+ oldFileName
    with open(newFileName, 'w', encoding="utf=8") as f:
        f.write(newContent)
    if retrieve_fileName:
        return newFileName

def SeperateFileFromDir(root_path):
    All_Lists = os.listdir(root_path)
    File_List = []	
    Dir_List = [root_path, ]	

    for item in All_Lists:
        item = os.path.join(root_path, item)
        if os.path.isfile(item):
            File_List.append(item)
        else:
            Dir_List.append(item)
    return File_List, Dir_List
"""
FILE IO METHODS
"""


if __name__ == '__main__':
    print("THIS IS FILE UTILITIES MODULE")
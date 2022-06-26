import os


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

"""
FILE IO METHODS
"""


if __name__ == '__main__':
    print("THIS IS FILE UTILITIES MODULE")
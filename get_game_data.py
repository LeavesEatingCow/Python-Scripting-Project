import os   #   Operating System
import json #   JSON Files
import shutil   #   Copy/Overwrite
from subprocess import PIPE, run    #   Allows Terminal functionalty
import sys  #   Get access to command line arguments

if __name__ == "__main__":
    args = sys.argv #   Variable will store command line arguments

    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")
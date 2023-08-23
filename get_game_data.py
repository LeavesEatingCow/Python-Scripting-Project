import os   #   Operating System
import json #   JSON Files
import shutil   #   Copy/Overwrite
from subprocess import PIPE, run    #   Allows Terminal functionalty
import sys  #   Get access to command line arguments

GAME_DIR_PATTERN = "game"   #   Lookfor string "game" in any directory

def find_all_game_paths(source):
    game_paths = []
    #os.walk() recursively goes through its arguments directiry and returns its root, its directories, and its files
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
        break

    return game_paths

def main(source, target):
    cwd = os.getcwrd()  #   Gets current Working Directory
    source_path = os.path.join(cwd, source) #   Use os.path.join and never string cocat
    target_path = os.path.join(cwd, target)

if __name__ == "__main__":
    args = sys.argv #   Variable will store command line arguments

    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")
    
    source, target = args[1:]
    main(source, target)
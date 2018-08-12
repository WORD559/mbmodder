# Warband directory autodetector

# I'll try and auto-detect game dir but I only know install dir for Linux GoG version
# If anyone knows other default install paths either submit a PR or put it in an issue

import os

user_dir = os.path.expanduser("~")

DEFAULTS = [
    user_dir+"/GOG Games/Mount Blade Warband",
    ]

def detect():
    for path in DEFAULTS:
        if os.path.isdir(path) and is_valid_dir(path):
            print "Detected Warband at '{path}'".format(path=path)
            return path
    valid = False
    while not valid: # If not autodetected, ask for input
        warband_dir = raw_input("Enter Mount and Blade: Warband directory:\n> ")
        while not os.path.isdir(warband_dir):
            print "Invalid directory"
            warband_dir = raw_input("Enter Mount and Blade: Warband directory:\n> ")
        while warband_dir[:-1] == "/" or warband_dir[:-1] == "\\":
            warband_dir = warband_dir[:-1]
        valid = is_valid_dir(warband_dir)
    return warband_dir

def is_valid_dir(warband_dir):
    return os.path.isdir(warband_dir+"/game")

# Warband directory autodetector

# I'll try and auto-detect game dir but I only know install dir for Linux GoG version
# If anyone knows other default install paths either submit a PR or put it in an issue

import os

user_dir = os.path.expanduser("~")

def detect_wb():
    DEFAULTS = [
        user_dir+"/GOG Games/Mount Blade Warband",
        #"steam/Steamapps/Common/mount and blade/modules",
    ]
    WIN_DEFAULTS = [
        "C:\\Program Files (x86)\\Mount and Blade",
        "C:\\Program Files\\Mount and Blade",
    ]
    if os.name == "win32":
        DEFAULTS += WIN_DEFAULTS
    for path in DEFAULTS:
        if os.path.isdir(path) and is_valid_dir(path):
            print "Detected Warband at '{path}'".format(path=path)
            return path
    return False

def is_valid_dir(warband_dir):
    return os.path.isdir(warband_dir+"/game")

def detect_cfg():
    # set Mount and Blade config directory (rgl_config.txt is here)
    if os.name == "win32": # not a Windows user so correct this if it's wrong
        config_dir = user_dir+"\\My Documents\\Mount&Blade Warband"
    else:
        config_dir = user_dir+"/.mbwarband"

    return config_dir

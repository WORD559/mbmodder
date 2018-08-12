#!/usr/bin/env python

## Mount and Blade: Warband modder

__version = "0.1.0"
__doc__ =\
"""Mount and Blade: Warband modder {version}.

Usage:
  mbmodder.py [-h] [-d directory] battle_size <num_units>

Options:
  -h --help                     Show this
  -d --warband-dir directory    Specify Warband install directory
  

""".format(version=__version)

import os

import dirdetector
from mods import *

from docopt import docopt
if __name__ == "__main__":
    arguments = docopt(__doc__,version=__version)
    #print arguments

# get user's home directory
user_dir = os.path.expanduser("~")

config_dir = dirdetector.detect_cfg()
if __name__ == "__main__":
    if arguments.has_key("--warband-dir") and arguments["--warband-dir"] != None:
        warband_dir = arguments["--warband-dir"] if dirdetector.is_valid_dir(arguments["--warband-dir"]) else 0
        if not warband_dir:
            print "Not a valid Warband directory -- exiting"
        while warband_dir[-1] == "/" or warband_dir[-1] == "\\":
            warband_dir = warband_dir[:-1]
    else:
        warband_dir = dirdetector.detect_wb()
else:
    warband_dir = dirdetector.detect_wb()
if not warband_dir:
    print "Warband not detected. Please specify install location with -d"

if arguments["battle_size"]:
    battle_sizer.battle_size(arguments["<num_units>"],config_dir)

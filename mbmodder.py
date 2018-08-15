#!/usr/bin/env python

## Mount and Blade: Warband modder

import os

import dirdetector
import mods

__version = "0.1.0"
options = "[-d directory]"
usages = ""

# Iterate through all mods and add their docopts to the __doc__
for mod in mods.__all__:
    mod = mods.__dict__[mod].mod
    usages += (mod.docopt + "\n")
__doc__ =\
"""Mount and Blade: Warband modder {version}.

Usage:
{usages}

Options:
  -h --help                     Show this
  -d --warband-dir directory    Specify Warband install directory
  

""".format(version=__version,usages=usages).format(options=options)

from docopt import docopt
if __name__ == "__main__":
    arguments = docopt(__doc__,version=__version)
    #print arguments

# get user's home directory and various dirs used by mods
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


# iterate through all the mods
if __name__ == "__main__":
    for mod in mods.__all__:
        mod = mods.__dict__[mod].mod
        if arguments.has_key(mod.name) and arguments[mod.name]: # if a mod has been selected
            # generate the args dict
            args = {}
            for arg in mod.arg_names:
                args[arg] = arguments["<"+arg+">"]
            # if either of the dirs are needed, pass them through
            if mod.needs_config:
                args["config_dir"] = config_dir
            if mod.needs_warband:
                args["warband_dir"] = warband_dir
            # finally, call the function and exit
            mod.function(**args)
            break

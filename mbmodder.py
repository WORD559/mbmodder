#!/usr/bin/env python2

## Mount and Blade: Warband modder

import os
import shutil

import dirdetector

# get user's home directory
user_dir = os.path.expanduser("~")

# set Mount and Blade config directory (rgl_config.txt is here)
if os.name == "win32": # not a Windows user so correct this if it's wrong
    config_dir = user_dir+"\\My Documents\\Mount&Blade Warband"
else:
    config_dir = user_dir+"/.mbwarband"

warband_dir = dirdetector.detect()

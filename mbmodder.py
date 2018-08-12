## Mount and Blade: Warband modder

import os
import shutil

if os.name == "win32": # not a Windows user so correct this if it's wrong
    config_dir = os.path.expanduser("~\\My Documents\\Mount&Blade Warband")
else:
    config_dir = os.path.expanduser("~/.mbwarband")


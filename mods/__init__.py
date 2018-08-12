import importlib,os

# get the globals
__globals = globals()

# list all mods
mods = os.listdir(os.path.dirname(__file__))

# add all found mods to __all__, so they can be got with "from mods import *"
__all__ = [i.strip(".py") for i in mods if i != "__init__.py" and i[-4:] != ".pyc" and i != "modframework.py"]

# import the mods so they can be accessed
for mod in __all__:
    __globals[mod] = importlib.import_module('.' + mod, package=__name__)

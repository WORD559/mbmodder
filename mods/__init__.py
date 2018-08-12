import importlib,os

__globals = globals()

mods = os.listdir(os.path.dirname(__file__))

__all__ = [i.strip(".py") for i in mods if i != "__init__.py" and i[-4:] != ".pyc" and i != "modframework.py"]

for mod in __all__:
    __globals[mod] = importlib.import_module('.' + mod, package=__name__)

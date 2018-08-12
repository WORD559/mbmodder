## mbmodder mod framework

class Mod(object):
    def __init__(self,function,name=None):
        self.name = name if name != None else function.func_code.co_name
        self.function = function
        self.docopt = ""
        self.num_args = function.func_code.co_argcount
        self.arg_names = list(function.func_code.co_varnames[:self.num_args])
        if "config_dir" in self.arg_names:
            self.needs_config = True
            self.arg_names.remove("config_dir")
        else: self.needs_config = False
        if "warband_dir" in self.arg_names:
            self.needs_warband = True
            self.arg_names.remove("warband_dir")
        else: self.needs_warband = False
        
        self.generate_docopt()

    def generate_docopt(self):
        self.docopt = "  mbmodder.py {options} {name}".format(name=self.name,options="{options}")
        for arg in self.arg_names:
            self.docopt += " <{varname}>".format(varname=arg)


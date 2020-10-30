# Main module in the code that will be used to filter which other modules will be used

import cmds.helpcmd
import cmds.mathcmd

modules_list = dir(cmds)

def run_process(name, *args):
    if name in modules_list: 
        if len(args) > 0:
            getattr(cmds, name).func(*args)
        else:
            getattr(cmds, name).func()
    else:
        print("Service not found")

def list_processes():
    for module in modules_list:
        print(module)

# Main module in the code that will be used to filter which other modules will be used

import helpcmd

modules_list = dir()

def run_process(name):
    if name in modules_list:
        getattr(globals()[name], "func")()

def list_processes():
    for module in modules_list:
        print(module)

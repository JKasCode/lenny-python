# Main module in the code that will be used to filter which other modules will be used

import cmds
import formatting

with open("service-list", "r") as service_list_file:
    services = service_list_file.readlines()

service_enabled = []
service_names = []
for service in services: # Splits and sorts the services
    split_service = service.split("-")
    service_names.append(split_service[0])
    service_enabled.append(split_service[1].rstrip()) # Get rid of that annoying \n

def run_process(service, child, *args):
    if service in service_names: 
        if service_enabled[service_names.index(service)] == "enabled": # Checks if the service is enabled
            if len(args) > 0:
                getattr(cmds, service)[child](*args)
            else:
                getattr(cmds, service)[child]()
        else:
            print("This service is disabled. Type the command \"services\" to enable it.")
    else:
        print("Service not found")

def list_processes(): # List and toggle services
    print("\nType the name of any service to enable/disable them if they're causing issues. Type \"cancel\" to cancel this.")
    for service in service_names:
        print(service + " - " + service_enabled[service_names.index(service)])
    
    user_input = input("[S] ")
    user_input = formatting.format_input(user_input)

    if user_input == "cancel":
        print("Cancelled\n")

    if user_input in service_names:
        service_e = service_enabled[service_names.index(user_input)]

        if service_e == "enabled":
            service_e = "disabled"
        else:
            service_e = "enabled"

        services[service_names.index(user_input)] = user_input+"-"+service_e+"\n" # Overwrite file with new preferences
        with open("service-list", "w") as service_file_w:
            service_file_w.writelines(services)

        service_enabled[service_names.index(user_input)] = service_e # Sets local variable to disabled so that user doesn't have to reset for effect to kick in
        print(user_input + " " + service_e+"\n")
    else:
        if user_input != "cancel":
            print("I couldn't find a service by that name!\n")

def get_commands():
    return cmds.commands

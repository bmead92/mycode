#!/usr/bin/env python3

# import for fun colors
import crayons
import json

# function for rebooting
def devicereboot(iplist):
    for ip in iplist:
        print(f'Connecting to... {ip}')
    print("REBOOTING NOW!")
    return None

# function to push commands
def commandpush(devicecmd): # dictionary

    for ip in devicecmd.keys():
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}')
        for mycmds in devicecmd[ip]:
            print(f"Attempting to send command --> {mycmds}")
    return None

# main function
def main():
    """called at runtime"""

    # json file
    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile) # decode JSON -> Python

    print(f'Welcome to the {crayons.blue("network")} device command pusher') # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    devicereboot(devicecmd.keys())
if __name__ == "__main__":
    main()

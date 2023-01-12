#!/usr/bin/env python3 

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # index to keep the dnsfile object open
    # create list of lines
    dnslist = dnsfile.readlines()
    # loop over lines
    for server in dnslist:
        print(server, end="")
# no need to close file, it's done automatically

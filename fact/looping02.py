#!/user/bin/env python3

# open file in read mode
dnsfile = open("dnsservers.txt", "r")

# create list of lines 
dnslist = dnsfile.readlines()

# loop over lines
for server in dnslist:
    # print and end without a newline
    print(server, end="") # line from file already has a newline built in

# close the file that we created
dnsfile.close()

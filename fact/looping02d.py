# open file in read mode
with open('dnsservers.txt', 'r') as dnsfile:
    # indent to keep the dnsfile object open
    # loop across the lines of the file
    for server in dnsfile:
        server = server.rstrip('\n') # removes newline char
        # if the server ends with org, place in org file
        if server.endswith('org'):
            with open('org-domain.txt', 'a') as serverfile:
                serverfile.write(server + '\n')
        # if it ends in com, send to a com file
        elif server.endswith('com'):
            with open('com-domain.txt', 'a') as serverfile:
                serverfile.write(server + '\n')
# auto closes

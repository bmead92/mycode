#!/usr/bin/env python3
## create file object in "r"ead mode

## user input for file reading
user_file = input("Enter the name of the file you'd like to read: \n")

## line counter
line_count = 0
with open(user_file, "r") as configfile:
    ## readlines() creates a list by reading the target file line by line
    configlist = configfile.readlines()
    for line in configlist:
        line_count += 1
## file is auto closed because 'with' was used

## each item of the list now has the newline char back
print(configlist)
print("Number of lines read: ", line_count)

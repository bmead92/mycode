#!/usr/bin/env python3

# parse the keystone.common.wsgi and return the number of failed login attempts

login_fail_counter = 0

# open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# turn the file into a list of lines in memory
keystone_file_lines = keystone_file.readlines()

# loop over the list of lines

for line in keystone_file_lines:
    #if this 'fail pattern' appears in the line, increment the count
    if "- - - - -] Authorization failed" in line:
        login_fail_counter += 1
    # display number of failed attempts
print("The number of failed login attempts is", login_fail_counter)
# always close the file when done working
keystone_file.close()

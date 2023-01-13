#!/usr/bin/env python3

# import just the call method from the subprocess module
from subprocess import call

# use call() to reveal the interfaces
call(["ip", "link", "show", "up"])

print("This program will check your interfaces.")

# prompt the user for an interface they'd like more details on

interface = input("Enter an interface, like, ens3: \n")

# use the input to issue ip addr show dev, revealing IPv4 IPv6 details
call(["ip", "addr", "show", "dev", interface])

# use input to issue ip route show dev
call(["ip", "route", "show", "dev", interface])



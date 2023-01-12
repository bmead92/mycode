#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
    learning about for logic"""

# create a list of vendors
vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'artista']

# create a list of approved vendors
approved_vendors = ['cisco', 'juniper', 'big_ip']
# loop across vendors

for vendor in vendors:
    print('The vendor is:' + vendor)
    if vendor not in approved_vendors:
        print("  - NOT AN APPROVED VENDOR!", end="")
print('\nLoop has ended')



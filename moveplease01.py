#!/usr/bin/env python3

# imports to complete our task
import shutil
import os

# move to specific directory
os.chdir('/home/student/mycode/')


def main():
    # move a file to a location
    shutil.move('raynor.obj', 'ceph_storage/')

    # user of user input to name kerrigan.obj file
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()

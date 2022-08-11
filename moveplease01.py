#!/usr/bin/env python3

import shutil
import os

def main():
    """called at runtime"""

    os.chdir('/home/student/mycode/')

    # moves first arg into second arg directory
    shutil.move('raynor-new.obj', 'ceph_storage/')

    #asks the user to rename the moved file puts it in variable
    xname = input('What is the new name for kerrigan.obj? ')


    #takes the old file in new dir and gives it the new name variable
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()

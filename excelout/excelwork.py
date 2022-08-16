#!/usr/bin/env python3

import pyexcel

def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("\nWat is the driver for the device? ")
    d = {"IP": input_ip, "driver": input_driver}
    return d

myListDict = []

print("Hello! This program will make you an *.xls file")

while(True):
    myListDict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue, or \ type 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=myListDict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")

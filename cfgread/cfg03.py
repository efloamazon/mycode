#!/usr/bin/env python3

commands = vlanconfig.cfg

with open("vlanconfig.cfg", "r") as configfile:
    configlist = configfile.readlines()

print(configlist)

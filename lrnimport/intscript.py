#!/usr/bin/env python3

from subprocess import call

call(["ip", "link", "show", "up"])

print("this program willc heck your interfaces")

interface = input("enter an interace, like, ense3: ")

call(["ip", "addr", "show", "dev", interface])

call(["ip", "route", "show", "dev", interface])


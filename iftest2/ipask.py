#!/usr/bin/env python3

ipchk = input("Apply an IP address")

if ipchk == "192.168.70.1":
    print("looks like the IP address was set: " + ipchk + "this isn't recommended")
elif ipchk:
    print("looks like IP address is: " + ipchk)
else:
    print("you did not provide input")

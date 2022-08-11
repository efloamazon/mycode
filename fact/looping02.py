#!/usr/bin/env python3

# open file in read mode
dnsfile = open("dnsservers.txt", "r")

# create list of lines
dnslist = dnsfile.readlines()

# loop over the lines
for svr in dnslist:
    #print and end witout new line
    print(svr, end="")
#Close the file (we created a list of lines)
dnsfile.close()

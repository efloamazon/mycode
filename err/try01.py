#!/usr/bin/env python3

while True:
    try:
        print("enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("no problemo")
        break
    except:
        print("error with file name try again")

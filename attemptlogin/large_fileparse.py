#!/usr/bin/python3

loginfail = 0

keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

for line in keystone_file:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print("the number of login fails is", loginfail)
keystone_file.close()

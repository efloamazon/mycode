#!/usr/bin/env python3

loginfail = 0
successful = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
        elif "-] Authorization failed" in line:
            successful += 1
print("the number of login fails is", loginfail)
print("the number of successful logins is", successful)

#!/usr/bin/env python3

message = "Your teacher says: "

testScore = float(input("Please enter your test score to get your teacher's comments: "))

if testScore >= 70:
    message = message + "Good job, you passed!"
elif testScore >= 50:
    message = message + "Oof, better luck next time"
else:
    message = message + "Yikes, time to start actually studying"


print(message)

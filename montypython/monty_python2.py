#!/usr/bin/env python3

round = 0
answer = " "

while round < 3 and answer != "Brian":
    round += 1
    answer = input('finish the movie title, "Monty Python\'s The Life of _____"')
    answer = answer.capitalize()
    if answer == 'Brian':
        print('Corrent')
    elif round == 3:
        print("Sorry the answer was Brian")

    else:
        print("Sorry! Try again!")

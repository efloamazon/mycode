#!/usr/bin/env python3

"""Random Poem Generator program"""

import os
import random

## Writting the poems as .txt files to be randomly selected by the program
def poem_gen():

    save_path = '/home/student/mycode/pythonproject-poem/randPoems'
    with open('Poem_1.txt', 'w') as poem1:
        poem1.write('"My code fails\n')
        poem1.write('I do not know why.\n')
        poem1.write('My code works.\n')
        poem1.write('I do not know why"\n')

    with open('Poem_2.txt', 'w') as poem2:
        poem2.write('"There was a young fellow who thought\n')
        poem2.write('Very little but thought it a lot.\n')
        poem2.write('Then at long last he knew\n')
        poem2.write('What he wanted to do,\n')
        poem2.write('But before he could start, he forgot"\n')

    with open('Poem_3.txt', 'w') as poem3:
        poem3.write('"I scaffolded it\n')
        poem3.write('I coded it\n')
        poem3.write('I refactored it\n')
        poem3.write('I tested it\n')
        poem3.write('I deployed it\n')
        poem3.write('I need a beer"\n')

    with open('Poem_4.txt', 'w') as poem4:
        poem4.write('"You don\'t open source your code\n')
        poem4.write(' Because it makes you money.\n')
        poem4.write(' I don\'t open source my code\n')
        poem4.write(' Because it is embarrassing...\n')
        poem4.write(' We are not the same"\n')

## Welcome message with instructions for users to generate a random poem
def poem_menu():
    print('\nWelcome to the Random Poem Generator App!')
    text = input('press "ENTER" to generate a poem!')

    if text == "":
        
        
        random_poem = random.choice(os.listdir('/home/student/mycode/pythonproject-poem'))
        with open(random_poem) as f:
            file_contents = f.read()
            print(file_contents)
            ## Random line from random poem
            lines = file_contents.split('\n')
            line = random.choice(lines)
            print(line)
            
    else:
        print('\nOops! Please ONLY press "ENTER" to generate a poem!')
        poem_menu()
poem_menu()

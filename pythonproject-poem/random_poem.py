#!/usr/bin/env python3

def main():
    with open('Poem_1.txt', 'w') as poem1:
        poem1.write('"My code fails.\n')
        poem1.write('I do not know why.\n')
        poem1.write('My code works.\n')
        poem1.write('I do not know why"\n')

main()

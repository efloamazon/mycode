#!/usr/bin/env python3

import re

import requests

def main():
    """Search a website's content"""

    print("where should we search?")
    url = input("> ")
    print(f"Great! So we'll try to open this URL {url} to search for the phrase:")

    
    searchFor = input("> ")

    resp = requests.get(url)
    searchMe = resp.text

    if re.search(searchFor, searchMe):
        print("Found a match!")
    else:
        print("no match!")
if __name__  == "__main__":
    main()

#!/usr/bin/env python3

vendors = ["cisco", "juniper", "big_ip", "f5", "artista", "alta3", "zach", "stuart"]

approved_vendors = ["cisco", "juniper", "big_ip"]

for x in vendors:
    print("\nThe vendor is " + x, end="")
    if x not in approved_vendors:
        print(" - NOT AN APOPROVED VENDOR!", end="")
print("\nOur loop has ended.")





farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


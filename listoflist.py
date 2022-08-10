#!/usr/bin/env python3

mexicanFood = ["tacos", "burritos", "salsa"]
bbqFood = ["hot dogs", "hamburgers", "fries"]
lifeFood = ["IPA", "Lager", "Any beer that's free"]

favoriteFoods = [mexicanFood] + [bbqFood] + [lifeFood]

print(favoriteFoods)

favFood = favoriteFoods[2][2]
print(f"my favorite food is: {favFood}!")


Superman = {
        "Suit Color": "blue",
        "Cape": True
    }

Elastigirl = {
        "Suit Color": "red",
        "Cape": False
        }

IronGiant = {
        "Suit Color": "silver",
        "Cape": False
        }

print( Superman.keys() )
print( Superman.values() )


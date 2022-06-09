#!/usr/bin/env python3
inventory = {"Axe":1, "Fruit":3,"Knife":2}

print(inventory)
for key, value in inventory.items() :
    print("Got "+str(value)+" "+str(key))
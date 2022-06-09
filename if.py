#!/usr/bin/env python3
pos = 5
key = "l"

if key == "r":
    pos += 1
    print("Player moved right")
elif key == "l":
    pos -= 1
    print("Player moved left")
else:
    print("Invalid key")
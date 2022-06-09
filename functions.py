#!/usr/bin/env python3

def move(pos, nb_steps):
    new_pos = pos + nb_steps
    return new_pos

pos = 5

print("Before: "+str(pos))

new_pos = move(pos,2)

print("After: "+str(new_pos))
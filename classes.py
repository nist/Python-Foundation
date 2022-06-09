#!/usr/bin/env python3
class GameCharacter:

    def __init__(self, name, pos, health) -> None:
        self.name = name
        self.pos = pos
        self.health = health

    def move(self, increment):
        self.pos += increment

character = GameCharacter("Nimish", 5, 100)

print(character.name)
print("Initial position:"+str(character.pos))
print("Moving...")
character.move(12)
print("Changed position:"+str(character.pos))
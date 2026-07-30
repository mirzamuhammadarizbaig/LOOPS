import random
rooms=["kitchen","basement","attic","garden","garage"]
treasureroom=random.choice(rooms)
found=False
while not found:
    room=input(f"Choose a room to search {rooms}: ")
    if room==treasureroom:
        print("You found the treasure!")
        found=True
    else:
        print("No treasure here, try again")

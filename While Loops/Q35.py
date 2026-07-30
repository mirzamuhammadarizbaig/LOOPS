treasureroom="attic"
found=False
while not found:
    room=input("Choose a room to search (kitchen, basement, attic, garden, garage): ")
    if room==treasureroom:
        print("You found the treasure!")
        found=True
    else:
        print("No treasure here, try again")

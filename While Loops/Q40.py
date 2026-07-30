import random
hunger=100
while hunger>0:
    hunger-=10
    print(f"Hunger level: {hunger}")
    if random.randint(1,5)==1:
        print("You found food!")
        hunger=100
if hunger<=0:
    print("You starved. Game over")

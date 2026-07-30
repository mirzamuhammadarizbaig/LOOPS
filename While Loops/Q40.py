hunger=100
while hunger>0:
    hunger-=10
    print(f"Hunger level: {hunger}")
    foundfood=input("Did you find food? (yes/no): ")
    if foundfood=="yes":
        hunger=100
if hunger<=0:
    print("You starved. Game over")

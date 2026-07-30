health=100
hunger=100
water=100
energy=100
running=True
while running:
    print(f"Health: {health}, Hunger: {hunger}, Water: {water}, Energy: {energy}")
    action=input(
        "1.Eat\n"
        "2.Drink\n"
        "3.Sleep\n"
        "4.Explore\n"
        "Choose an Option: "
    )
    if action=="1":
        hunger=min(100,hunger+20)
    elif action=="2":
        water=min(100,water+20)
    elif action=="3":
        energy=min(100,energy+20)
    elif action=="4":
        gothurt=input("Did you get hurt while exploring? (yes/no): ")
        if gothurt=="yes":
            health-=15
            print("You got hurt while exploring!")
        else:
            print("Exploration was safe")
    else:
        print("Invalid Choice")
    hunger-=10
    water-=10
    energy-=10
    if hunger<0:
        hunger=0
    if water<0:
        water=0
    if energy<0:
        energy=0
    if health<=0 or hunger<=0 or water<=0 or energy<=0:
        running=False
        print("A stat reached zero, game over")

health=100
hunger=100

while True:
    choice=input(
        "1.Eat\n"
        "2.Rest\n"
        "3.Explore\n"
        "4.Exit\n"
    )

    if choice=="1":
        hunger=hunger+20
        print("Hunger level :",hunger)

    elif choice=="2":
        health=health+10
        print("Health level :",health)

    elif choice=="3":
        hunger=hunger-15
        health=health-5
        print("You explored, hunger :",hunger,"health :",health)

    elif choice=="4":
        print("Thank you for playing")
        break

    else:
        print("Invalid choice")
        continue

    if hunger<=0 or health<=0:
        print("You did not survive, game over")
        break

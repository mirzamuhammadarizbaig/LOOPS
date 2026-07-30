while True:
    choice=input(
        "You are standing at a crossroad.\n"
        "1.Go Left\n"
        "2.Go Right\n"
        "3.Exit\n"
    )

    if choice=="1":
        print("You found a river and had to turn back")

    elif choice=="2":
        print("You found a treasure chest, you win!")
        break

    elif choice=="3":
        print("Thank you for playing")
        break

    else:
        print("Invalid choice")

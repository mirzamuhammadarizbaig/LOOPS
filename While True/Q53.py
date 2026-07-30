fuel=100

while True:
    choice=input(
        "1.Drive\n"
        "2.Refuel\n"
        "3.Check Fuel\n"
        "4.Exit\n"
    )

    if choice=="1":
        if fuel<=0:
            print("Out of fuel, you cannot drive")
        else:
            fuel=fuel-10
            print("You drove some distance, fuel left is",fuel)

    elif choice=="2":
        fuel=100
        print("Tank refueled to 100")

    elif choice=="3":
        print("Current fuel is",fuel)

    elif choice=="4":
        print("Thank you for playing")
        break

    else:
        print("Invalid choice")

while True:
    choice=input(
        "1.Km to Miles\n"
        "2.Miles to Km\n"
        "3.Exit\n"
    )

    if choice=="1":
        km=float(input("Enter distance in Km : "))
        miles=km*0.621371
        print("Distance in Miles is",miles)

    elif choice=="2":
        miles=float(input("Enter distance in Miles : "))
        km=miles/0.621371
        print("Distance in Km is",km)

    elif choice=="3":
        print("Thank you for using this program")
        break

    else:
        print("Invalid choice")

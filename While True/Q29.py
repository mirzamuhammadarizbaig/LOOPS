while True:
    choice=input(
        "1.Recharge 100\n"
        "2.Recharge 200\n"
        "3.Recharge 500\n"
        "4.Exit\n"
    )

    if choice=="1":
        print("Recharged with Rs.100, validity 1 day")

    elif choice=="2":
        print("Recharged with Rs.200, validity 7 days")

    elif choice=="3":
        print("Recharged with Rs.500, validity 30 days")

    elif choice=="4":
        print("Thank you for using this recharge system")
        break

    else:
        print("Invalid choice")

total=0

while True:
    choice=input(
        "1.Burger - 300\n"
        "2.Pizza - 800\n"
        "3.Drink - 100\n"
        "4.Checkout\n"
    )

    if choice=="1":
        total=total+300
        print("Burger added")

    elif choice=="2":
        total=total+800
        print("Pizza added")

    elif choice=="3":
        total=total+100
        print("Drink added")

    elif choice=="4":
        print("Your total bill is",total)
        break

    else:
        print("Invalid choice")

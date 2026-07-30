stock=50

while True:
    choice=input(
        "1.Add Stock\n"
        "2.Remove Stock\n"
        "3.Check Stock\n"
        "4.Exit\n"
    )

    if choice=="1":
        amount=int(input("Enter quantity to add : "))
        stock=stock+amount
        print("Stock updated, current stock is",stock)

    elif choice=="2":
        amount=int(input("Enter quantity to remove : "))
        if amount>stock:
            print("Not enough stock available")
        else:
            stock=stock-amount
            print("Stock updated, current stock is",stock)

    elif choice=="3":
        print("Current stock is",stock)

    elif choice=="4":
        print("Thank you for using this program")
        break

    else:
        print("Invalid choice")

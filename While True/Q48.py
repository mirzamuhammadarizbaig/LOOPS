while True:
    choice=input(
        "1.USD to PKR\n"
        "2.PKR to USD\n"
        "3.Exit\n"
    )

    if choice=="1":
        amount=float(input("Enter amount in USD : "))
        converted=amount*278
        print("Amount in PKR is",converted)

    elif choice=="2":
        amount=float(input("Enter amount in PKR : "))
        converted=amount/278
        print("Amount in USD is",converted)

    elif choice=="3":
        print("Thank you for using this program")
        break

    else:
        print("Invalid choice")

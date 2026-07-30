savings=0

while True:
    choice=input(
        "1.Add Money\n"
        "2.Check Savings\n"
        "3.Exit\n"
    )

    if choice=="1":
        amount=int(input("Enter amount to add : "))
        savings=savings+amount
        print("Total savings is",savings)

    elif choice=="2":
        print("Your savings is",savings)

    elif choice=="3":
        print("Thank you for using this program")
        break

    else:
        print("Invalid choice")

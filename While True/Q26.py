balance=1000

while True:
    choice=input(
        "1.Check Balance\n"
        "2.Deposit\n"
        "3.Withdraw\n"
        "4.Exit\n"
    )

    if choice=="1":
        print("Your balance is",balance)

    elif choice=="2":
        amount=int(input("Enter amount to deposit : "))
        balance=balance+amount
        print("New balance is",balance)

    elif choice=="3":
        amount=int(input("Enter amount to withdraw : "))
        if amount>balance:
            print("Insufficient balance")
        else:
            balance=balance-amount
            print("New balance is",balance)

    elif choice=="4":
        print("Thank you for using this ATM")
        break

    else:
        print("Invalid choice")

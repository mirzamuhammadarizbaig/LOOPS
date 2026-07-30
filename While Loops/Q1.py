balance=1000
running=True

while running:
    choice=input(
        "1.Check Balance\n"
        "2.Withdraw\n"
        "3.Deposit\n"
        "4.Exit\n"
        "Choose an Option: "
    )

    if choice=="1":
        print(f"Your account balance is ${balance}")

    elif choice=="2":
        amount=float(input("Enter the amount you want to Withdraw: "))
        if amount<=balance:
            balance-=amount
            print("Succesfully withdraw")
            print(f"Current balance {balance}")
        else:
            print("Insufficiant Amount")

    elif choice=="3":
        amount1=float(input("Enter the amount you want to Deposit: "))
        balance+=amount1
        print("Succesfull Deposit")
        print(f"Current Balance {balance}")

    elif choice=="4":
        print("Thank you for using our ATM")
        running=False

    else:
      print("Invalid Choice")
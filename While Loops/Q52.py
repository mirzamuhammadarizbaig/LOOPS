balance=0
running=True
while running:
    choice=input(
        "1.Deposit\n"
        "2.Withdraw\n"
        "3.Balance\n"
        "4.Exit\n"
        "Choose an Option: "
    )
    if choice=="1":
        amount=float(input("Enter amount to deposit: "))
        balance+=amount
        print(f"Deposit successful, balance is {balance}")
    elif choice=="2":
        amount=float(input("Enter amount to withdraw: "))
        if amount<=balance:
            balance-=amount
            print(f"Withdrawal successful, balance is {balance}")
        else:
            print("Insufficient balance")
    elif choice=="3":
        print(f"Your balance is {balance}")
    elif choice=="4":
        print("Thank you for banking with us")
        running=False
    else:
        print("Invalid Choice")

balance = 100
choice = 0

while choice != 4:

    print("\n--- Mobile Recharge System ---")
    print("1. Check Balance")
    print("2. Recharge")
    print("3. Use Internet")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your Balance:", balance)

    elif choice == 2:
        recharge = int(input("Enter recharge amount: "))
        balance += recharge
        print("Recharge Successful!")

    elif choice == 3:
        usage = int(input("Enter internet cost: "))

        if usage <= balance:
            balance -= usage
            print("Internet Used!")
        else:
            print("Insufficient Balance!")

    elif choice == 4:
        print("System Closed")

    else:
        print("Invalid Choice!")
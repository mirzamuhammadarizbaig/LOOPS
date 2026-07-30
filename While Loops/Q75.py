money = 0
choice = 0

while choice != 4:

    print("\n--- Money Saver Tracker ---")
    print("1. Add Money")
    print("2. Spend Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_money = int(input("Enter money to add: "))

        money += add_money

        print("Money Added Successfully!")
        print("Current Balance:", money)


    elif choice == 2:
        spend_money = int(input("Enter money to spend: "))

        if spend_money <= money:
            money -= spend_money
            print("Money Spent Successfully!")
            print("Remaining Balance:", money)

        else:
            print("Not Enough Money!")


    elif choice == 3:
        print("Your Total Savings:", money)


    elif choice == 4:
        print("Saving Tracker Closed!")


    else:
        print("Invalid Choice!")
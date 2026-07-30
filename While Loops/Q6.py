balance = 20
running = True

while running:

    choice = input(
        "\n1. Chips ($5)\n"
        "2. Chocolate ($7)\n"
        "3. Juice ($4)\n"
        "4. Exit\n"
        "Choose an item: "
    )

    if choice == "1":

        if balance >= 5:
            balance -= 5
            print("You bought Chips.")
            print(f"Remaining Balance: ${balance}")
        else:
            print("Insufficient Balance!")

    elif choice == "2":

        if balance >= 7:
            balance -= 7
            print("You bought Chocolate.")
            print(f"Remaining Balance: ${balance}")
        else:
            print("Insufficient Balance!")

    elif choice == "3":

        if balance >= 4:
            balance -= 4
            print("You bought Juice.")
            print(f"Remaining Balance: ${balance}")
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank you for using the Vending Machine!")
        running = False

    else:
        print("Invalid Choice!")
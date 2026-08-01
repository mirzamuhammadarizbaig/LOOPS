running = True

while running:
    choice = input(
        "\n1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        "5. Exit\n"
        "Choose an option: "
    )
    if choice == "5":
        print("Calculator Closed!")
        running = False
    elif choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "1":
            print("Answer:", num1 + num2)

        elif choice == "2":
            print("Answer:", num1 - num2)

        elif choice == "3":
            print("Answer:", num1 * num2)

        elif choice == "4":

            if num2 != 0:
                print("Answer:", num1 / num2)
            else:
                print("Cannot divide by zero!")

    else:
        print("Invalid Choice!")
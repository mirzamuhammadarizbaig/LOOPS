while True:
    num1=int(input("Enter the first number (0 to exit) : "))
    num2=int(input("Enter the second number : "))

    if num1=="0":
        break

    choice=input(
        "1.Addition\n"
        "2.Subtraction\n"
        "3.Multiplication\n"
        "4.Division\n"
        "5.Exit\n"
    )

    if choice=="1":
        add=num1+num2
        print(add)

    elif choice=="2":
        sub=num1-num2
        print(sub)

    elif choice=="3":
        mul=num1*num2
        print(mul)

    elif choice=="4":
        div=num1/num2
        print(div)

    elif choice=="5":
        print("Thank you for using this calc")
        break

    else:
        print("Invalid choice")


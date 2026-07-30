running=True
while running:
    choice=input(
        "1.Add\n"
        "2.Subtract\n"
        "3.Multiply\n"
        "4.Divide\n"
        "5.Exit\n"
        "Choose an Option: "
    )
    if choice=="5":
        print("Exiting Calculator")
        running=False
    elif choice in ["1","2","3","4"]:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        if choice=="1":
            print(f"Result: {num1+num2}")
        elif choice=="2":
            print(f"Result: {num1-num2}")
        elif choice=="3":
            print(f"Result: {num1*num2}")
        elif choice=="4":
            if num2!=0:
                print(f"Result: {num1/num2}")
            else:
                print("Cannot divide by zero")
    else:
        print("Invalid Choice")

lights="off"
fan="off"
door="locked"

while True:
    choice=input(
        "1.Toggle Lights\n"
        "2.Toggle Fan\n"
        "3.Toggle Door\n"
        "4.Check Status\n"
        "5.Exit\n"
    )

    if choice=="1":
        if lights=="off":
            lights="on"
        else:
            lights="off"
        print("Lights are now",lights)

    elif choice=="2":
        if fan=="off":
            fan="on"
        else:
            fan="off"
        print("Fan is now",fan)

    elif choice=="3":
        if door=="locked":
            door="unlocked"
        else:
            door="locked"
        print("Door is now",door)

    elif choice=="4":
        print("Lights :",lights,"Fan :",fan,"Door :",door)

    elif choice=="5":
        print("Thank you for using this program")
        break

    else:
        print("Invalid choice")

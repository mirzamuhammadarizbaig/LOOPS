price_per_night=2000
rooms_left=10

while True:
    choice=input(
        "1.Book Room\n"
        "2.Check Rooms Left\n"
        "3.Exit\n"
    )

    if choice=="1":
        if rooms_left<=0:
            print("Sorry, no rooms left")
        else:
            nights=int(input("Enter number of nights : "))
            total=nights*price_per_night
            rooms_left=rooms_left-1
            print("Total price is",total)

    elif choice=="2":
        print("Rooms left :",rooms_left)

    elif choice=="3":
        print("Thank you for booking with us")
        break

    else:
        print("Invalid choice")

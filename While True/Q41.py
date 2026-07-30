price=100
seats_left=40

while True:
    choice=input(
        "1.Book Ticket\n"
        "2.Check Seats Left\n"
        "3.Exit\n"
    )

    if choice=="1":
        if seats_left<=0:
            print("Sorry, bus is full")
        else:
            tickets=int(input("Enter number of tickets : "))
            if tickets>seats_left:
                print("Not enough seats available")
            else:
                seats_left=seats_left-tickets
                total=tickets*price
                print("Total price is",total)

    elif choice=="2":
        print("Seats left :",seats_left)

    elif choice=="3":
        print("Thank you for booking with us")
        break

    else:
        print("Invalid choice")

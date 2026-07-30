rooms={}
running=True
while running:
    choice=input(
        "1.Book Room\n"
        "2.Cancel Booking\n"
        "3.View Bookings\n"
        "4.Exit\n"
        "Choose an Option: "
    )
    if choice=="1":
        name=input("Enter guest name: ")
        roomno=input("Enter room number: ")
        rooms[roomno]=name
        print("Room booked successfully")
    elif choice=="2":
        roomno=input("Enter room number to cancel: ")
        if roomno in rooms:
            del rooms[roomno]
            print("Booking cancelled")
        else:
            print("Booking not found")
    elif choice=="3":
        print("Current Bookings:",rooms)
    elif choice=="4":
        print("Exiting Hotel Reservation System")
        running=False
    else:
        print("Invalid Choice")

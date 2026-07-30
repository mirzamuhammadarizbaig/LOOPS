seats=list(range(1,21))
booked=[]
running=True
while running:
    choice=input(
        "1.Book Ticket\n"
        "2.Cancel Ticket\n"
        "3.View Available Seats\n"
        "4.Exit\n"
        "Choose an Option: "
    )
    if choice=="1":
        seat=int(input("Enter seat number to book: "))
        if seat in seats:
            seats.remove(seat)
            booked.append(seat)
            print("Seat booked successfully")
        else:
            print("Seat not available")
    elif choice=="2":
        seat=int(input("Enter seat number to cancel: "))
        if seat in booked:
            booked.remove(seat)
            seats.append(seat)
            print("Booking cancelled")
        else:
            print("Seat not found in bookings")
    elif choice=="3":
        print("Available Seats:",seats)
    elif choice=="4":
        print("Exiting Movie Ticket Booking")
        running=False
    else:
        print("Invalid Choice")

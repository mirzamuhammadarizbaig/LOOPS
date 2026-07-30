books_available=5

while True:
    choice=input(
        "1.Issue Book\n"
        "2.Return Book\n"
        "3.Check Available Books\n"
        "4.Exit\n"
    )

    if choice=="1":
        if books_available<=0:
            print("No books available")
        else:
            books_available=books_available-1
            print("Book issued successfully")

    elif choice=="2":
        books_available=books_available+1
        print("Book returned successfully")

    elif choice=="3":
        print("Books available :",books_available)

    elif choice=="4":
        print("Thank you for using this library system")
        break

    else:
        print("Invalid choice")

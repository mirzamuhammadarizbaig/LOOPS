books=["Python Basics","Data Structures","Web Development"]
running=True
while running:
    choice=input(
        "1.Issue Book\n"
        "2.Return Book\n"
        "3.View Books\n"
        "4.Exit\n"
        "Choose an Option: "
    )
    if choice=="1":
        book=input("Enter book name to issue: ")
        if book in books:
            books.remove(book)
            print("Book issued successfully")
        else:
            print("Book not available")
    elif choice=="2":
        book=input("Enter book name to return: ")
        books.append(book)
        print("Book returned successfully")
    elif choice=="3":
        print("Available Books:",books)
    elif choice=="4":
        print("Exiting Library Management System")
        running=False
    else:
        print("Invalid Choice")

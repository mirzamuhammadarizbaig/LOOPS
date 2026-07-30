saved_name=""
saved_number=""

while True:
    choice=input(
        "1.Save Contact\n"
        "2.View Contact\n"
        "3.Exit\n"
    )

    if choice=="1":
        saved_name=input("Enter contact name : ")
        saved_number=input("Enter contact number : ")
        print("Contact saved")

    elif choice=="2":
        if saved_name=="":
            print("No contact saved yet")
        else:
            print("Name :",saved_name)
            print("Number :",saved_number)

    elif choice=="3":
        print("Thank you for using this program")
        break

    else:
        print("Invalid choice")

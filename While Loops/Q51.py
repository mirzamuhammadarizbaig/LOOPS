students=[]
running=True
while running:
    choice=input(
        "1.Add Student\n"
        "2.Remove Student\n"
        "3.View Students\n"
        "4.Exit\n"
        "Choose an Option: "
    )
    if choice=="1":
        name=input("Enter student name: ")
        students.append(name)
        print("Student added")
    elif choice=="2":
        name=input("Enter student name to remove: ")
        if name in students:
            students.remove(name)
            print("Student removed")
        else:
            print("Student not found")
    elif choice=="3":
        print("Students:",students)
    elif choice=="4":
        print("Exiting Student Management System")
        running=False
    else:
        print("Invalid Choice")

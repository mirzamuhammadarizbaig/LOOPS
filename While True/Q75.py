present = 0
absent = 0

while True:

    print("1. Mark Present")
    print("2. Mark Absent")
    print("3. Show Attendance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        present += 1
        print("Student marked Present.")

    elif choice == 2:
        absent += 1
        print("Student marked Absent.")

    elif choice == 3:
        total = present + absent

        print("Present Students:", present)
        print("Absent Students:", absent)
        print("Total Students:", total)

    elif choice == 4:
        print("Attendance System Closed.")
        break

    else:
        print("Invalid Choice.")
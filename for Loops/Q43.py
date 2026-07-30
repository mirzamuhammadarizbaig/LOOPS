n = int(input("How many students?: "))
presentCount = 0

for i in range(1, n+1):
    name = input(f"Enter student {i} name: ")
    status = input(f"Is {name} present? (y/n): ").lower()
    if status == "y":
        presentCount += 1
        print(f"{name} marked Present")
    else:
        print(f"{name} marked Absent")

attendancePercent = (presentCount / n) * 100
print("Total Present:", presentCount)
print("Attendance %:", attendancePercent)

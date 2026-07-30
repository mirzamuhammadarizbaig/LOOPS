topper_name = ""
topper_avg = 0

for i in range(1, 16):
    name = input(f"Enter name of student {i}: ")
    total = 0

    for s in range(1, 6):
        marks = float(input(f"  Enter marks for subject {s}: "))
        total += marks

    average = total / 5

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: Total={total}, Average={average:.2f}, Grade={grade}")

    if average > topper_avg:
        topper_avg = average
        topper_name = name

print("Topper is", topper_name, "with average", topper_avg)

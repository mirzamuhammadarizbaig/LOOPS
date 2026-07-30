while True:
    marks=int(input("Enter your marks (-1 to exit) : "))

    if marks==-1:
        print("Thank you for using this program")
        break

    if marks>=90:
        grade="A"
    elif marks>=80:
        grade="B"
    elif marks>=70:
        grade="C"
    elif marks>=60:
        grade="D"
    else:
        grade="F"

    print("Your grade is",grade)

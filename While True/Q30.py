while True:
    name=input("Enter student name (or type exit) : ")

    if name=="exit":
        print("Thank you for using this program")
        break

    marks1=int(input("Enter marks in subject 1 : "))
    marks2=int(input("Enter marks in subject 2 : "))
    marks3=int(input("Enter marks in subject 3 : "))

    total=marks1+marks2+marks3
    percentage=total/3

    if percentage>=80:
        grade="A"
    elif percentage>=60:
        grade="B"
    elif percentage>=40:
        grade="C"
    else:
        grade="F"

    print("Total marks is",total)
    print("Percentage is",percentage)
    print("Grade is",grade)

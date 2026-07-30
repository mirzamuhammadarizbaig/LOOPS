while True:
    income=input("Enter your monthly income (or type exit) : ")

    if income=="exit":
        print("Thank you for using this program")
        break

    income=int(income)
    age=int(input("Enter your age : "))

    if age<18:
        print("Not eligible, age must be 18 or above")
    elif income<30000:
        print("Not eligible, income too low")
    else:
        print("You are eligible for a loan")

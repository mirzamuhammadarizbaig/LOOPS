while True:
    count=int(input("Enter a number to countdown from : "))

    while count>=0:
        print(count)
        count=count-1

    choice=input("Do you want to restart? (yes/no) : ")

    if choice=="no":
        print("Thank you for using this program")
        break

while True:
    num=input("Enter a number (or type exit) : ")

    if num=="exit":
        print("Thank you for using this program")
        break

    num=int(num)

    if num>0:
        print("Positive number")
    elif num<0:
        print("Negative number")
    else:
        print("Zero")

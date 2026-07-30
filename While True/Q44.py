while True:
    units=input("Enter units consumed (or type exit) : ")

    if units=="exit":
        print("Thank you for using this program")
        break

    units=int(units)

    if units<=100:
        bill=units*5
    elif units<=300:
        bill=units*7
    else:
        bill=units*10

    print("Your electricity bill is",bill)

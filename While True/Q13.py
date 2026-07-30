while True:
    temp=input("Enter the temperature (or type stop to exit) : ")

    if temp=="stop":
        print("Thank you for using this program")
        break

    temp=int(temp)

    if temp>40:
        print("It is very hot")
    elif temp>30:
        print("It is hot")
    elif temp>20:
        print("It is warm")
    elif temp>10:
        print("It is cold")
    else:
        print("It is very cold")

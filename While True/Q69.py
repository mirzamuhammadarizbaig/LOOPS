current_floor=1

while True:
    choice=input("Enter floor number to go to (or type exit) : ")

    if choice=="exit":
        print("Thank you for using this elevator")
        break

    floor=int(choice)

    if floor==current_floor:
        print("You are already on this floor")
    elif floor>current_floor:
        print("Going up to floor",floor)
        current_floor=floor
    else:
        print("Going down to floor",floor)
        current_floor=floor

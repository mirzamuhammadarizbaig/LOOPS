temprature=0

while True:
    choice=input("Enter the temprature (w to exit)\n")

    if choice=="w":
        print("Thank you for using us")
        break

    temprature=int(choice)

    if temprature>40:
        print("Very HOT")

    elif temprature>30:
        print("Hot")

    elif temprature>20:
        print("Warm")

    elif temprature>10:
        print("Cold")

    else:
        print("Very Cold")
light="red"

while True:
    choice=input("Press n for next light or e to exit : ")

    if choice=="e":
        print("Thank you for using this program")
        break

    elif choice=="n":
        if light=="red":
            light="green"
        elif light=="green":
            light="yellow"
        elif light=="yellow":
            light="red"

        print("Light is now",light)

    else:
        print("Invalid choice")

distance=0
finish_line=100

while True:
    choice=input("Press g to accelerate or s to stop : ")

    if choice=="g":
        distance=distance+10
        print("Distance covered :",distance)

        if distance>=finish_line:
            print("You reached the finish line, you win!")
            break

    elif choice=="s":
        print("You stopped the race")
        break

    else:
        print("Invalid choice")

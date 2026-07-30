battery = 100
distance = 0

while True:

    print("1. Move Forward")
    print("2. Move Backward")
    print("3. Turn Left")
    print("4. Turn Right")
    print("5. Charge Battery")
    print("6. Check Battery")
    print("7. Check Distance")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if battery >= 10:
            battery -= 10
            distance += 5
            print("Robot moved forward.")
        else:
            print("Battery too low! Please charge the robot.")

    elif choice == 2:

        if battery >= 10:
            battery -= 10
            print("Robot moved backward.")
        else:
            print("Battery too low! Please charge the robot.")

    elif choice == 3:

        if battery >= 5:
            battery -= 5
            print("Robot turned left.")
        else:
            print("Battery too low! Please charge the robot.")

    elif choice == 4:

        if battery >= 5:
            battery -= 5
            print("Robot turned right.")
        else:
            print("Battery too low! Please charge the robot.")

    elif choice == 5:
        battery = 100
        print("Battery fully charged!")

    elif choice == 6:
        print("Battery:", battery, "%")

    elif choice == 7:
        print("Distance Travelled:", distance, "meters")

    elif choice == 8:
        print("Robot Shutdown...")
        break

    else:
        print("Invalid Choice!")
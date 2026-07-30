health = 100
hunger = 50
energy = 50

while True:

    print("1. Feed Pet")
    print("2. Let Pet Sleep")
    print("3. Play")
    print("4. Check Status")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hunger -= 20

        if hunger < 0:
            hunger = 0

        print("Pet has been fed.")

    elif choice == 2:
        energy = 100
        print("Pet is sleeping.")

    elif choice == 3:

        if energy >= 20:
            energy -= 20
            hunger += 10
            health += 5

            if health > 100:
                health = 100

            print("Pet enjoyed playing.")
        else:
            print("Pet is too tired.")

    elif choice == 4:
        print("Health:", health)
        print("Hunger:", hunger)
        print("Energy:", energy)

    elif choice == 5:
        print("Game Closed.")
        break

    else:
        print("Invalid Choice.")
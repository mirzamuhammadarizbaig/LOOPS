health = 100
gold = 50

while True:

    print("1. Go to Forest")
    print("2. Visit Village")
    print("3. Fight Monster")
    print("4. Show Status")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        gold += 20
        print("You found 20 gold.")

    elif choice == 2:

        if gold >= 10:
            gold -= 10
            health += 10

            if health > 100:
                health = 100

            print("You bought food.")
        else:
            print("Not enough gold.")

    elif choice == 3:

        if health >= 20:
            health -= 20
            gold += 50
            print("Monster defeated.")
        else:
            print("Your health is too low.")

    elif choice == 4:
        print("Health:", health)
        print("Gold:", gold)

    elif choice == 5:
        print("Adventure Ended.")
        break

    else:
        print("Invalid Choice.")
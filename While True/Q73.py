age = 18
money = 1000
health = 100

while True:
    
    print("1. Work")
    print("2. Eat")
    print("3. Sleep")
    print("4. Show Status")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        money += 500
        health -= 10
        age += 1
        print("You worked for one year.")

    elif choice == 2:

        if money >= 200:
            money -= 200
            health += 10

            if health > 100:
                health = 100

            print("You ate food.")
        else:
            print("Not enough money.")

    elif choice == 3:
        health += 20

        if health > 100:
            health = 100

        print("You slept well.")

    elif choice == 4:
        print("Age:", age)
        print("Money:", money)
        print("Health:", health)

    elif choice == 5:
        print("Life Simulator Closed.")
        break

    else:
        print("Invalid Choice.")
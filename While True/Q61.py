enemy_ships=5
fuel=100

while True:
    choice=input(
        "1.Shoot\n"
        "2.Move\n"
        "3.Exit\n"
    )

    if choice=="1":
        if enemy_ships<=0:
            print("No enemies left")
        else:
            enemy_ships=enemy_ships-1
            print("Enemy destroyed, ships left :",enemy_ships)

        if enemy_ships<=0:
            print("You cleared all enemies, you win!")
            break

    elif choice=="2":
        fuel=fuel-10
        print("Fuel left :",fuel)

        if fuel<=0:
            print("Out of fuel, game over")
            break

    elif choice=="3":
        print("Thank you for playing")
        break

    else:
        print("Invalid choice")

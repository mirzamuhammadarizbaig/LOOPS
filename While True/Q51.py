player_health=100
zombie_health=50

while True:
    choice=input(
        "1.Attack\n"
        "2.Run Away\n"
    )

    if choice=="1":
        zombie_health=zombie_health-10
        player_health=player_health-5
        print("Zombie health :",zombie_health)
        print("Your health :",player_health)

        if zombie_health<=0:
            print("You killed the zombie, you win!")
            break

        if player_health<=0:
            print("The zombie killed you, game over")
            break

    elif choice=="2":
        print("You ran away safely")
        break

    else:
        print("Invalid choice")

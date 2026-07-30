your_monster_hp=60
enemy_monster_hp=60

while True:
    choice=input(
        "1.Attack\n"
        "2.Defend\n"
        "3.Exit\n"
    )

    if choice=="1":
        enemy_monster_hp=enemy_monster_hp-12
        print("Enemy monster HP :",enemy_monster_hp)

        if enemy_monster_hp<=0:
            print("Enemy monster fainted, you win!")
            break

        your_monster_hp=your_monster_hp-8
        print("Your monster HP :",your_monster_hp)

        if your_monster_hp<=0:
            print("Your monster fainted, you lose!")
            break

    elif choice=="2":
        print("Your monster defended the attack")

    elif choice=="3":
        print("Thank you for playing")
        break

    else:
        print("Invalid choice")

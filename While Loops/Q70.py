import random
health=100
gold=50
inventory=[]
running=True
while running:
    print(f"Health: {health}, Gold: {gold}, Inventory: {inventory}")
    choice=input(
        "1.Battle Enemy\n"
        "2.Visit Shop\n"
        "3.Heal\n"
        "4.Boss Fight\n"
        "5.Save Score\n"
        "6.Exit\n"
        "Choose an Option: "
    )
    if choice=="1":
        enemyhealth=30
        while enemyhealth>0 and health>0:
            damage=random.randint(5,15)
            enemyhealth-=damage
            enemydamage=random.randint(3,10)
            health-=enemydamage
            print(f"You dealt {damage} damage, enemy dealt {enemydamage} damage")
        if health>0:
            gold+=20
            print("You defeated the enemy and earned 20 gold")
        else:
            print("You were defeated")
            running=False
    elif choice=="2":
        if gold>=15:
            gold-=15
            inventory.append("Potion")
            print("You bought a Potion")
        else:
            print("Not enough gold")
    elif choice=="3":
        if "Potion" in inventory:
            inventory.remove("Potion")
            health=min(100,health+30)
            print("You healed using a Potion")
        else:
            print("No potions in inventory")
    elif choice=="4":
        bosshealth=80
        while bosshealth>0 and health>0:
            damage=random.randint(5,20)
            bosshealth-=damage
            bossdamage=random.randint(5,15)
            health-=bossdamage
            print(f"You dealt {damage} damage, boss dealt {bossdamage} damage")
        if health>0:
            print("You defeated the final boss! You win the game!")
            running=False
        else:
            print("The boss defeated you")
            running=False
    elif choice=="5":
        print(f"Score saved: Gold={gold}, Health={health}")
    elif choice=="6":
        print("Exiting RPG Adventure Game")
        running=False
    else:
        print("Invalid Choice")
    if health<=0:
        print("You have died. Game over")
        running=False

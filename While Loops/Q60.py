plans={"1":("Basic",10),"2":("Standard",20),"3":("Premium",30)}
balance=0
running=True
while running:
    choice=input(
        "1.View Plans\n"
        "2.Recharge\n"
        "3.Check Balance\n"
        "4.Exit\n"
        "Choose an Option: "
    )
    if choice=="1":
        keys=list(plans.keys())
        i=0
        while i<len(keys):
            print(f"{keys[i]}. {plans[keys[i]][0]} - ${plans[keys[i]][1]}")
            i+=1
    elif choice=="2":
        plan=input("Enter plan number to recharge: ")
        if plan in plans:
            balance+=plans[plan][1]
            print(f"Recharge successful, balance is {balance}")
        else:
            print("Invalid plan")
    elif choice=="3":
        print(f"Your balance is {balance}")
    elif choice=="4":
        print("Exiting Mobile Recharge System")
        running=False
    else:
        print("Invalid Choice")

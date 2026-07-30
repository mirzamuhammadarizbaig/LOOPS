slots=10
occupied=0
running=True
while running:
    choice=input(
        "1.Park Vehicle\n"
        "2.Remove Vehicle\n"
        "3.View Available Slots\n"
        "4.Exit\n"
        "Choose an Option: "
    )
    if choice=="1":
        if occupied<slots:
            occupied+=1
            print("Vehicle parked successfully")
        else:
            print("Parking full")
    elif choice=="2":
        if occupied>0:
            occupied-=1
            print("Vehicle removed successfully")
        else:
            print("No vehicles parked")
    elif choice=="3":
        print(f"Available slots: {slots-occupied}")
    elif choice=="4":
        print("Exiting Parking Management System")
        running=False
    else:
        print("Invalid Choice")

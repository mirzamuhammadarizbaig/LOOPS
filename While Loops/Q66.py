currentfloor=1
running=True
while running:
    print(f"Current floor: {currentfloor}")
    choice=input("Enter floor number to go to (or 'exit' to quit): ")
    if choice=="exit":
        print("Exiting elevator")
        running=False
    else:
        targetfloor=int(choice)
        while currentfloor!=targetfloor:
            if currentfloor<targetfloor:
                currentfloor+=1
            else:
                currentfloor-=1
            print(f"Passing floor {currentfloor}")
        print(f"Arrived at floor {currentfloor}")

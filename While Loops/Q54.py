cart=[]
running=True
while running:
    choice=input(
        "1.Add Item\n"
        "2.Remove Item\n"
        "3.Checkout\n"
        "4.Exit\n"
        "Choose an Option: "
    )
    if choice=="1":
        item=input("Enter item name: ")
        cart.append(item)
        print("Item added")
    elif choice=="2":
        item=input("Enter item name to remove: ")
        if item in cart:
            cart.remove(item)
            print("Item removed")
        else:
            print("Item not found")
    elif choice=="3":
        print("Your cart:",cart)
        print("Checkout complete, thank you for shopping")
        cart=[]
    elif choice=="4":
        print("Exiting Shopping Cart")
        running=False
    else:
        print("Invalid Choice")

menu={"burger":5,"pizza":8,"pasta":7,"soda":2}
order=[]
running=True
while running:
    choice=input(
        "1.Add Item\n"
        "2.View Order\n"
        "3.Checkout\n"
        "4.Exit\n"
        "Choose an Option: "
    )
    if choice=="1":
        item=input(f"Enter item from menu {list(menu.keys())}: ")
        if item in menu:
            order.append(item)
            print("Item added to order")
        else:
            print("Item not on menu")
    elif choice=="2":
        print("Your order:",order)
    elif choice=="3":
        total=0
        i=0
        while i<len(order):
            total+=menu[order[i]]
            i+=1
        print(f"Total bill: ${total}")
        order=[]
    elif choice=="4":
        print("Exiting Restaurant Ordering System")
        running=False
    else:
        print("Invalid Choice")

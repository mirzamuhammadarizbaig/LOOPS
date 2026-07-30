items={"chips":2,"soda":3,"chocolate":2,"water":1}
balance=10
running=True
while running and balance>0:
    print(f"Your balance is ${balance}")
    item=input(f"Choose an item {list(items.keys())} or 'exit': ")
    if item=="exit":
        running=False
    elif item in items:
        if items[item]<=balance:
            balance-=items[item]
            print(f"You bought {item}, remaining balance ${balance}")
        else:
            print("Insufficient balance")
    else:
        print("Item not available")
if balance<=0:
    print("Balance is empty, vending machine session ended")

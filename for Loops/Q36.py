n=int(input("How many items: "))
total=0
for i in range(1,n+1):
    itemName=input(f"Enter item {i} name: ")
    price=float(input(f"Enter the Price of {itemName}: "))
    qty=int(input(f"Enter the quantity of {itemName}: "))
    itemTotal= price*qty
    total+=itemTotal
print("Total",total)
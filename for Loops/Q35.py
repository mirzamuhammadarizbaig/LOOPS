n=int(input("How many items?: "))
total=0
for i in range(1,n+1):
    name=input(f"Enter item {i} name: ")
    price=int(input(f"Price of {name}: "))
    qty=int(input(f"Enter the quantity of {name}: "))
    itemTotal= price*qty
    total+=itemTotal
    print(f"{name}: {qty} x {price} = {itemTotal}")
print("Grand Total =",total)
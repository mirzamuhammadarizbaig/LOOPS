n = int(input("How many items?: "))
total = 0

for i in range(1, n+1):
    item = input(f"Enter item {i} name: ")
    price = float(input(f"Price of {item}: "))
    qty = int(input(f"Quantity of {item}: "))
    itemTotal = price * qty
    total += itemTotal
    print(f"{item}: {qty} x {price} = {itemTotal}")

if total > 1000:
    discount = total * 0.10
    finalTotal = total - discount
    print("Subtotal:", total)
    print("Discount (10%):", discount)
    print("Final Total:", finalTotal)
else:
    print("Total (no discount):", total)

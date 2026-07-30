n = int(input("How many items?: "))
grand_total = 0

for i in range(1, n+1):
    item = input(f"Enter item {i} name: ")
    qty = int(input(f"Enter quantity of {item}: "))
    price = float(input(f"Enter price per unit of {item}: "))

    subtotal = 0
    for q in range(qty):
        subtotal += price

    grand_total += subtotal
    print(f"{item}: Qty={qty}, Subtotal={subtotal}")

print("Final Bill:", grand_total)

total_inventory = 0
low_stock = 0
threshold = 10

for i in range(1, 41):
    product = input(f"Enter name of product {i}: ")
    stock = int(input(f"Enter stock quantity for {product}: "))

    total_inventory += stock

    if stock < threshold:
        low_stock += 1
        print(f"{product}: LOW STOCK ({stock})")
    else:
        print(f"{product}: Stock={stock}")

print("Total Inventory:", total_inventory)
print("Low Stock Items:", low_stock)

n = int(input("How many dishes ordered?: "))
total = 0

for i in range(1, n+1):
    dish = input(f"Enter dish {i} name: ")
    price = float(input(f"Price of {dish}: "))
    qty = int(input(f"Quantity of {dish}: "))
    dishTotal = price * qty
    total += dishTotal
    print(f"{dish}: {qty} x {price} = {dishTotal}")

tax = total * 0.05
grandTotal = total + tax

print("Subtotal:", total)
print("Tax (5%):", tax)
print("Grand Total:", grandTotal)

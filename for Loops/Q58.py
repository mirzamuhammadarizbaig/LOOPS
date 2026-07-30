grand_total = 0

for i in range(1, 26):
    name = input(f"Enter name of patient {i}: ")
    bill = float(input(f"Enter bill amount for {name}: "))

    if bill >= 20000:
        discount = bill * 0.20
    elif bill >= 10000:
        discount = bill * 0.10
    elif bill >= 5000:
        discount = bill * 0.05
    else:
        discount = 0

    final = bill - discount
    grand_total += final

    print(f"{name}: Bill={bill}, Discount={discount}, Final={final}")

print("Grand Total:", grand_total)

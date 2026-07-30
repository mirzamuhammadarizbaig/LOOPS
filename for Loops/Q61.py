grand_total = 0
highest_order = 0
highest_customer = ""

for i in range(1, 21):
    name = input(f"Enter name of customer {i}: ")
    amount = float(input(f"Enter order total for {name}: "))
    discount = float(input(f"Any discount % for {name}? (0 if none): "))

    final = amount - (amount * discount / 100)
    grand_total += final

    print(f"{name}: Order={amount}, Final={final}")

    if final > highest_order:
        highest_order = final
        highest_customer = name

print("Grand Total:", grand_total)
print("Most Expensive Order:", highest_customer, "-", highest_order)

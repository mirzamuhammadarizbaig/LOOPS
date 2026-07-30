n = int(input("How many expenses this month?: "))
total = 0

for i in range(1, n+1):
    category = input(f"Enter category for expense {i} (e.g. Food, Rent): ")
    amount = float(input(f"Amount spent on {category}: "))
    total += amount
    print(f"{category}: {amount}")

print("Total Monthly Expense:", total)

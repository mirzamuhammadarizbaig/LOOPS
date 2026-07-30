monthly_revenue = 0
highest_sale = 0
highest_day = 0

for day in range(1, 32):
    sale = float(input(f"Enter sales for day {day}: "))
    monthly_revenue += sale

    if sale > highest_sale:
        highest_sale = sale
        highest_day = day

print("Monthly Revenue:", monthly_revenue)
print("Highest Selling Day:", highest_day, "with sales", highest_sale)

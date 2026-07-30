economy = 0
business = 0
first_class = 0
revenue = 0

economy_price = 15000
business_price = 35000
first_price = 60000

for i in range(1, 101):
    seat_class = input(f"Passenger {i} - Class (economy/business/first): ")

    if seat_class.lower() == "economy":
        economy += 1
        revenue += economy_price
    elif seat_class.lower() == "business":
        business += 1
        revenue += business_price
    elif seat_class.lower() == "first":
        first_class += 1
        revenue += first_price

print("Economy Bookings:", economy)
print("Business Bookings:", business)
print("First Class Bookings:", first_class)
print("Total Revenue:", revenue)

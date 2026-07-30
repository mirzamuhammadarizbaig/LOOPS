revenue = 0
vip_count = 0
booked = 0
vip_price = 1000
normal_price = 500

for seat in range(1, 51):
    status = input(f"Seat {seat} - Book seat? (yes/no): ")

    if status.lower() == "yes":
        booked += 1
        seat_type = input(f"  Seat {seat} - Type (vip/normal): ")

        if seat_type.lower() == "vip":
            revenue += vip_price
            vip_count += 1
        else:
            revenue += normal_price

remaining = 50 - booked

print("Total Revenue:", revenue)
print("VIP Bookings:", vip_count)
print("Remaining Seats:", remaining)

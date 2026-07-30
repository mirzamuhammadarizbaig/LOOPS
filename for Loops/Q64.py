booked = 0

for seat in range(1, 41):
    status = input(f"Seat {seat} - Book? (yes/no): ")
    if status.lower() == "yes":
        booked += 1

empty = 40 - booked
occupancy = (booked / 40) * 100

print("Booked Seats:", booked)
print("Empty Seats:", empty)
print("Occupancy Percentage:", occupancy)

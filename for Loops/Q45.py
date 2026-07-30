n = int(input("How many rides today?: "))
baseFare = 50
perKmRate = 20
totalEarnings = 0

for i in range(1, n+1):
    distance = float(input(f"Enter distance for ride {i} (km): "))
    fare = baseFare + (distance * perKmRate)
    totalEarnings += fare
    print(f"Ride {i}: {distance} km, Fare = {fare}")

print("Total Earnings Today:", totalEarnings)

n = int(input("How many vehicles?: "))
baseFee = 30
perHourRate = 15
totalCollected = 0

for i in range(1, n+1):
    vehicle = input(f"Enter vehicle {i} number plate: ")
    hours = float(input(f"Hours parked by {vehicle}: "))
    fee = baseFee + (hours * perHourRate)
    totalCollected += fee
    print(f"{vehicle}: {hours} hrs, Fee = {fee}")

print("Total Collected:", totalCollected)

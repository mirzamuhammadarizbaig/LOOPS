total_collected = 0

for i in range(1, 26):
    house = input(f"Enter house number {i}: ")
    units = float(input(f"Enter units consumed for house {house}: "))

    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = 100 * 5 + (units - 100) * 8
    else:
        bill = 100 * 5 + 200 * 8 + (units - 300) * 12

    total_collected += bill
    print(f"House {house}: Units={units}, Bill={bill}")

print("Total Revenue Collected:", total_collected)

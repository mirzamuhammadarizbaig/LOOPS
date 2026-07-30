n = int(input("How many households?: "))

for i in range(1, n+1):
    name = input(f"Enter household {i} name: ")
    units = int(input(f"Units consumed by {name}: "))

    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = (100 * 5) + (units - 100) * 8
    else:
        bill = (100 * 5) + (200 * 8) + (units - 300) * 12

    print(f"{name}: {units} units, Bill = {bill}")

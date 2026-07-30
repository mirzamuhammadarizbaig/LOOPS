n = int(input("How many books returned?: "))
totalFine = 0
finePerDay = 10

for i in range(1, n+1):
    book = input(f"Enter book {i} name: ")
    daysLate = int(input(f"How many days late is {book}?: "))
    if daysLate > 0:
        fine = daysLate * finePerDay
        totalFine += fine
        print(f"{book} is late by {daysLate} days, fine = {fine}")
    else:
        print(f"{book} returned on time, no fine")

print("Total Fine Collected:", totalFine)

total_fine = 0
fine_per_day = 10

for i in range(1, 51):
    book = input(f"Enter title of book {i}: ")
    late_days = int(input(f"Enter late days for {book}: "))

    if late_days > 0:
        fine = late_days * fine_per_day
    else:
        fine = 0

    total_fine += fine
    print(f"{book}: Late Days={late_days}, Fine={fine}")

print("Total Fine Collected:", total_fine)

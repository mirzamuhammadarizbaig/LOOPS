total_temp = 0
hottest = -1000
coldest = 1000
rainy_days = 0

for day in range(1, 31):
    temp = float(input(f"Enter temperature for day {day}: "))
    rain = input(f"Was it rainy on day {day}? (yes/no): ")

    total_temp += temp

    if temp > hottest:
        hottest = temp
    if temp < coldest:
        coldest = temp
    if rain.lower() == "yes":
        rainy_days += 1

average = total_temp / 30

print("Average Temperature:", round(average, 2))
print("Hottest Day:", hottest)
print("Coldest Day:", coldest)
print("Rainy Days:", rainy_days)

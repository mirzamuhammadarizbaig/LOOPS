total_wpm = 0
fastest = 0
slowest = 10000
fastest_name = ""
slowest_name = ""

for i in range(1, 16):
    name = input(f"Enter name of contestant {i}: ")
    wpm = float(input(f"Enter WPM for {name}: "))

    total_wpm += wpm

    if wpm > fastest:
        fastest = wpm
        fastest_name = name
    if wpm < slowest:
        slowest = wpm
        slowest_name = name

average = total_wpm / 15

print("Fastest:", fastest_name, "-", fastest, "WPM")
print("Slowest:", slowest_name, "-", slowest, "WPM")
print("Average WPM:", round(average, 2))

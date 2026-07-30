names = []
times = []

for i in range(1, 13):
    name = input(f"Enter name of racer {i}: ")
    time = float(input(f"Enter finishing time (seconds) for {name}: "))
    names.append(name)
    times.append(time)

sorted_times = sorted(times)
first_time = sorted_times[0]
second_time = sorted_times[1]
third_time = sorted_times[2]

first_name = names[times.index(first_time)]
second_name = names[times.index(second_time)]
third_name = names[times.index(third_time)]

print("🥇 1st Place:", first_name, "-", first_time)
print("🥈 2nd Place:", second_name, "-", second_time)
print("🥉 3rd Place:", third_name, "-", third_time)

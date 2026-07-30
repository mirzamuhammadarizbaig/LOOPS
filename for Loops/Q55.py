total_runs = 0
fours = 0
sixes = 0
wickets = 0

for ball in range(1, 121):
    runs = input(f"Ball {ball} - Enter runs scored (or W for wicket): ")

    if runs.upper() == "W":
        wickets += 1
        print(f"Ball {ball}: WICKET!")
    else:
        runs = int(runs)
        total_runs += runs
        if runs == 4:
            fours += 1
        elif runs == 6:
            sixes += 1
        print(f"Ball {ball}: {runs} runs")

strike_rate = (total_runs / 120) * 100

print("Total Runs:", total_runs)
print("Fours:", fours)
print("Sixes:", sixes)
print("Wickets:", wickets)
print("Strike Rate:", round(strike_rate, 2))

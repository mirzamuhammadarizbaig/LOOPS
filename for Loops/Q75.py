fuel = 100
total_used = 0
emergency_stages = 0
mission_status = "SUCCESS"

for stage in range(1, 51):
    used = float(input(f"Stage {stage} - Enter fuel used: "))
    fuel -= used
    total_used += used

    if fuel <= 0:
        fuel = 0
        print(f"Stage {stage}: Fuel depleted! Mission aborted.")
        mission_status = "FAILED"
        break

    if fuel < 20:
        emergency_stages += 1
        print(f"Stage {stage}: EMERGENCY! Fuel low ({fuel})")
    else:
        print(f"Stage {stage}: Fuel remaining = {fuel}")

print("Total Fuel Used:", total_used)
print("Remaining Fuel:", fuel)
print("Emergency Stages:", emergency_stages)
print("Mission Status:", mission_status)

passed = 0
failed = 0
defective = 0

for i in range(1, 201):
    status = input(f"Product {i} - Status (pass/fail/defective): ")

    if status.lower() == "pass":
        passed += 1
    elif status.lower() == "fail":
        failed += 1
    elif status.lower() == "defective":
        defective += 1

defect_percentage = (defective / 200) * 100

print("Passed:", passed)
print("Failed:", failed)
print("Defective:", defective)
print("Defect Percentage:", round(defect_percentage, 2))

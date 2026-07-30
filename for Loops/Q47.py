n = int(input("How many questions?: "))
score = 0

for i in range(1, n+1):
    answer = input(f"Q{i}: Correct or Wrong? (c/w): ").lower()
    if answer == "c":
        score += 4
        print(f"Q{i}: Correct, +4")
    else:
        score -= 1
        print(f"Q{i}: Wrong, -1")

print("Final Score:", score)

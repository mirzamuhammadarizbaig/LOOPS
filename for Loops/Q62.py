score = 0

for i in range(1, 21):
    answer = input(f"Question {i} - Correct? (yes/no): ")
    if answer.lower() == "yes":
        score += 1

percentage = (score / 20) * 100

print("Score:", score, "/20")
print("Percentage:", percentage)

if percentage >= 90:
    medal = "Gold"
elif percentage >= 75:
    medal = "Silver"
elif percentage >= 50:
    medal = "Bronze"
else:
    medal = "No Medal"

print("Medal:", medal)

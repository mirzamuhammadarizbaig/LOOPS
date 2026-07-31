print("=====STUDENT MARKS=====\n")

number=int(input("Enter the number of subject: "))

total=0

for i in range(1, number + 1):
    marks = int(input(f"Enter marks of Subject {i}: "))
    total += marks

average= total / number

print("\n-----RESULT-----")
print(f"Total Marks = {total}")
print(f"Averge marks = {average}")
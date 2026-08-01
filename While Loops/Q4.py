score = 0
question = 1

while question <= 5:

    if question == 1:
        answer = input("1. Capital of Pakistan?: ").lower()

        if answer == "islamabad":
            print("Correct")
            score += 1
            question += 1
        else:
            print("Wrong")
            question += 1

    elif question == 2:
        answer = input("2. 5 x 6 = ? ")

        if answer == "30":
            print("Correct")
            score += 1
            question += 1
        else:
            print("Wrong")
            question += 1

    elif question == 3:
        answer = input("3. Is Python a programming language? ").lower()

        if answer == "yes":
            print("Correct")
            score += 1
            question += 1
        else:
            print("Wrong")
            question += 1

    elif question == 4:
        answer = input("4. How many days in a week? ")

        if answer == "7":
            print("Correct")
            score += 1
            question += 1
        else:
            print("Wrong")
            question += 1

    elif question == 5:
        answer = input("5. Which planet is known as the Red Planet? ").lower()

        if answer == "mars":
            print("Correct")
            score += 1
            question += 1
        else:
            print("Wrong")
            question += 1

print("\n----- RESULT -----")
print(f"You got {score}/5 correct.")
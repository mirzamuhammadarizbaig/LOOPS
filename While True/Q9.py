post="student"

while True:
    ask=input("Who are you? (student/politician/teacher): ").lower()
    if ask==post:
        print("Thanks for being honest")
        break

    else:
        print("LIER!")
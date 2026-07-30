target=57
guess=int(input("Guess the number (1-100): "))
while guess!=target:
    if guess<target:
        print("Too low")
    else:
        print("Too high")
    guess=int(input("Guess again: "))
print(f"Correct! The number was {target}")

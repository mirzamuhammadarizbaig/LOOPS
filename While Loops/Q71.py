secret_code = "4821"

health = 100      
trace = 0         
attempts = 0
score = 0

while trace < 100 and health > 0:
    print(f"\nAttempt {attempts + 1}")
    print(f"Firewall Health: {health}, Trace Level: {trace}, Score: {score}")

    guess = input("Enter 4-digit access code: ")
    attempts += 1

    if guess == secret_code:
        print("\nACCESS GRANTED! You cracked the mainframe!")
        score += 500
        break
    else:
        print("Acces denied")

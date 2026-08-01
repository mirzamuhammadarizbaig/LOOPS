number = int(input("Enter a number: "))

while number <= 0:

    print("Invalid! Please enter a positive number.")

    number = int(input("Enter a number: "))

print(f"{number} is a positive number.")
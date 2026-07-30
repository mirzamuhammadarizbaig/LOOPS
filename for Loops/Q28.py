count = 0
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    if num % 2 != 0:
        count += 1
print("Odd numbers:", count)
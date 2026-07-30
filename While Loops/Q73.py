evenCount = 0
oddCount = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    elif num % 2 == 0:
        evenCount += 1

    else:
        oddCount += 1


print("Even Numbers:", evenCount)
print("Odd Numbers:", oddCount)
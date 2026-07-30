largest = None
while True:
    num = input("Enter a number (or 'i' to stop): ")
    if num == "i":
        break
    num =int(num)
    if largest == None or num > largest:
        largest = num

print(f"The largest number entered is {largest}")
smallest = None
while True:
    num = input("Enter a number (or 'i' to stop): ")
    if num == "i":
        break
    num =int(num)
    if smallest == None or num < smallest:
        smallest = num

print(f"The smallest number entered is {smallest}")
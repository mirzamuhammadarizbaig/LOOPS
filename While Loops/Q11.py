num=int(input("Enter a number (0 to stop): "))
largest=num
while num!=0:
    if num>largest:
        largest=num
    num=int(input("Enter a number (0 to stop): "))
print(f"The largest number entered is {largest}")

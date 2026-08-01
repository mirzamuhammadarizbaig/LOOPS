largest=-1
second=-1
num=int(input("Enter a number (-1 to stop): "))
while num!=-1:
    if num>largest:
        second=largest
        largest=num
    elif num>second:
        second=num
    num=int(input("Enter a number (-1 to stop): "))
print(f"The second largest number entered is {second}")

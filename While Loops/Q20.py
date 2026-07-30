total=0
num=int(input("Enter a number (0 to stop): "))
while num!=0:
    total+=num
    print(f"Running total: {total}")
    num=int(input("Enter a number (0 to stop): "))
print(f"Final total: {total}")

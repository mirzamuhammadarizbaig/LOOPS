count=0
num=int(input("Enter a number (0 to stop): "))
while num!=0:
    if num%3==0 and num%5==0:
        count+=1
    num=int(input("Enter a number (0 to stop): "))
print(f"Numbers divisible by both 3 and 5: {count}")

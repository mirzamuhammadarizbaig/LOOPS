smallest=None
num=int(input("Enter a number (0 to stop): "))
while num!=0:
    if num%2!=0:
        if smallest==None or num<smallest:
            smallest=num
    num=int(input("Enter a number (0 to stop): "))
if smallest!=None:
    print(f"The smallest odd number entered is {smallest}")
else:
    print("No odd numbers entered")

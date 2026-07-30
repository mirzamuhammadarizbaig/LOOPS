streak=0
num=int(input("Enter a number: "))
while streak<5:
    if num%2==0:
        streak+=1
    else:
        streak=0
    if streak<5:
        num=int(input("Enter a number: "))
print("Five consecutive even numbers entered!")

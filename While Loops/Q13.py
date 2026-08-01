total=0
count=0
num=int(input("Enter a number (0 to stop): "))
while num!=0:
    if num>0:
        total+=num
        count+=1
    num=int(input("Enter a number (0 to stop): "))
if count>0:
    print(f"The average of positive numbers is {total/count}")
else:
    print("No positive numbers entered")

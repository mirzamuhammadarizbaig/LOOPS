total=0
count=0

while True:
    num=input("Enter a number (or type 0 to exit) : ")

    if num=="0":
        break

    num=int(num)
    total=total+num
    count=count+1

if count>0:
    average=total/count
    print("The average is",average)
else:
    print("No numbers entered")

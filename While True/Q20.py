while True:
    num=input("Enter a number (or type exit) : ")

    if num=="exit":
        print("Thank you for using this program")
        break

    count=0
    temp=int(num)

    if temp==0:
        count=1

    while temp!=0:
        temp=temp//10
        count=count+1

    print("Number of digits is",count)

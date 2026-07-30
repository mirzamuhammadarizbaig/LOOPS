while True:
    num=int(input("Enter a number (0 to exit) : "))

    if num==0:
        break

    reverse=0
    temp=num

    while temp!=0:
        digit=temp%10
        reverse=(reverse*10)+digit
        temp=temp//10

    print("Reversed number is",reverse)
